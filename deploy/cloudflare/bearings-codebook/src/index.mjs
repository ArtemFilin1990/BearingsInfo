import { VERIFIED_CODES, KNOWN_BRANDS } from './codebook.mjs';

const index = new Map(VERIFIED_CODES.map(c => [c.manufacturer+'|'+c.component+'|'+c.code,c]));
const headers = {'content-type':'application/json; charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff','referrer-policy':'no-referrer'};
function json(value,status=200){return new Response(JSON.stringify(value),{status,headers})}
function invalid(message,status=400){return json({error:message,auto_replace_allowed:false},status)}
function brandOf(b){return typeof b==='string'?b.trim().toUpperCase():''}
function safe(s,limit=96){return typeof s==='string'&&s.length<=limit&&/^[\w.\-/\s]+$/u.test(s)}
export function lookup(brand,code,component='suffix'){
  return index.get(brandOf(brand)+'|'+component+'|'+String(code||'').trim().toUpperCase())??null;
}
export function decode(brand,suffix){
  const b=brandOf(brand), s=String(suffix||'').trim().toUpperCase();
  if(!KNOWN_BRANDS.includes(b))return {brand:b||null,original_suffix:s,matched:[],unknown_parts:s?[s]:[],status:'UNKNOWN_BRAND',auto_replace_allowed:false};
  const candidates=VERIFIED_CODES.filter(c=>c.manufacturer===b&&c.component==='suffix').sort((a,b)=>b.code.length-a.code.length);
  let i=0;const matched=[],unknown_parts=[];
  while(i<s.length){
    if(' -/.'.includes(s[i])){i++;continue}
    const found=candidates.find(c=>s.startsWith(c.code,i));
    if(found){matched.push(found);i+=found.code.length;continue}
    let j=i+1;while(j<s.length&&!' -/.'.includes(s[j]))j++;
    unknown_parts.push(s.slice(i,j));i=j;
  }
  return {brand:b,original_suffix:s,matched,unknown_parts,status:!s?'EMPTY':unknown_parts.length?'REVIEW_UNKNOWN_CODE':'VERIFIED_CODE_SCOPE_REVIEW',auto_replace_allowed:false};
}
export function compare(left,right){
  const l=decode(left?.brand,left?.suffix),r=decode(right?.brand,right?.suffix);
  const full=x=>x.status==='VERIFIED_CODE_SCOPE_REVIEW'&&x.matched.length>0;
  const shapes=x=>x.matched.map(c=>c.feature+':'+c.contact_type+':'+c.sides).sort();
  const code_relationship=!full(l)||!full(r)?'INSUFFICIENT_CODE_EVIDENCE':
    JSON.stringify(shapes(l))===JSON.stringify(shapes(r))?'SAME_FEATURE_NOT_PROVEN_INTERCHANGEABLE':'DIFFERENT_TECHNICAL_FEATURE';
  return {left:l,right:r,code_relationship,product_equivalence:'NOT_ASSESSED',decision:'ENGINEER_REVIEW_REQUIRED',auto_replace_allowed:false,
    reasons:['OEM_CODE_MEANING_NOT_PRODUCT_SPECIFICATION','NO_SCOPED_ENGINEERING_APPROVAL']};
}
async function readSmallJSON(req){
  const length=Number(req.headers.get('content-length'));
  if(length>2048)throw Error('PAYLOAD_TOO_LARGE');
  if(!(req.headers.get('content-type')||'').toLowerCase().startsWith('application/json'))throw Error('JSON_ONLY');
  const reader=req.body?.getReader();
  if(!reader)throw Error('INVALID_JSON');
  const chunks=[];let bytesRead=0;
  while(true){
    const {done,value}=await reader.read();if(done)break;
    bytesRead+=value.byteLength;
    if(bytesRead>2048){await reader.cancel();throw Error('PAYLOAD_TOO_LARGE')}
    chunks.push(value);
  }
  const buffer=new Uint8Array(bytesRead);let pos=0;
  for(const chunk of chunks){buffer.set(chunk,pos);pos+=chunk.byteLength}
  const body=new TextDecoder().decode(buffer);
  let obj;try{obj=JSON.parse(body)}catch{throw Error('INVALID_JSON')}
  if(!obj||typeof obj!=='object'||Array.isArray(obj))throw Error('OBJECT_REQUIRED');
  return obj;
}

// Structural parsing only. ГОСТ↔ISO equivalence is never inferred from designation digits.
export function parseMarking(raw, declaredBrand='') {
  const raw_designation = typeof raw==='string' ? raw : '';
  const issues=[];
  const empty=() => ({raw_designation,brand:null,prefix:'',basic_designation:'',suffix:'',
    standard_hint:'UNKNOWN',parse_status:'INVALID',issues,source_codes:[],
    product_equivalence:'NOT_ASSESSED',auto_replace_allowed:false});
  if (!raw_designation.trim()||raw_designation.length>160 || !/^[A-ZА-ЯЁ0-9.\/\-\s]+$/u.test(raw_designation.toUpperCase())) {
    issues.push('INVALID_MARKING_INPUT');return empty();
  }
  let value=raw_designation.trim().toUpperCase().replace(/\s+/g,' ');
  value=value.replace(/^(?:ПОДШИПНИК|BEARING)\s+/, '');
  const detected=[];
  const atStart=KNOWN_BRANDS.find(b=>value.startsWith(b+' '));
  if(atStart){detected.push(atStart);value=value.slice(atStart.length+1).trim()}
  const atEnd=KNOWN_BRANDS.find(b=>value.endsWith(' '+b));
  if(atEnd){detected.push(atEnd);value=value.slice(0,-atEnd.length-1).trim()}
  const asserted=typeof declaredBrand==='string'?declaredBrand.trim().toUpperCase():'';
  if(asserted&&!KNOWN_BRANDS.includes(asserted)) issues.push('UNKNOWN_DECLARED_BRAND');
  const distinct=new Set([...detected, ...(asserted?[asserted]:[])]);
  if(distinct.size>1)issues.push('CONFLICTING_BRANDS');
  const brand=asserted||detected[0]||null;
  if(!brand)issues.push('BRAND_UNKNOWN');
  let prefix='', prefix_origin='NONE', standard_hint='UNVERIFIED';
  if(brand){
    const documented=VERIFIED_CODES.filter(c=>c.manufacturer===brand&&c.component==='prefix')
      .sort((a,b)=>b.code.length-a.code.length);
    const hit=documented.find(c=>value.startsWith(c.code));
    if(hit){prefix=hit.code;prefix_origin='OFFICIAL_CODE_ONLY';value=value.slice(hit.code.length);
      if(value.startsWith('-')){prefix+='-';value=value.slice(1)}value=value.trim();}
  }
  if(!prefix){const gost=/^(\d{1,2}-)(?=\d{3,7}(?:\D|$))/.exec(value);
    if(gost){prefix=gost[1];prefix_origin='STRUCTURAL_ONLY';value=value.slice(prefix.length);standard_hint='GOST_CANDIDATE';}}
  const genericFamilies=['NUP','RNA','NU','NJ','QJ','NA','HK','BK','UC','UK','N'];
  const family=genericFamilies.find(f=>new RegExp('^'+f+'\\d{2,7}').test(value));
  const bodyMatch=family?new RegExp('^('+family+'\\d{2,7})(.*)
  async fetch(req){
    try{
      const url=new URL(req.url),path=url.pathname;
      if(req.method==='GET'&&path==='/health')
        return json({service:'EVEREST BearingsInfo',status:'ok',mode:'read-only',code_count:VERIFIED_CODES.length,approved_product_analogues:0});
      if (path==='/v1/parse' && req.method==='POST') {
        const obj=await readSmallJSON(req);
        if (typeof obj.raw_designation!=='string'||obj.raw_designation.length>160||
            (obj.brand!==undefined&&typeof obj.brand!=='string'))return invalid('BAD_MARKING');
        return json(parseMarking(obj.raw_designation,obj.brand||''));
      }
      if(req.method==='GET'&&path==='/v1/lookup'){
        const brand=brandOf(url.searchParams.get('brand')),code=url.searchParams.get('code'),component=url.searchParams.get('component')||'suffix';
        if(!KNOWN_BRANDS.includes(brand)||!safe(code)||!['suffix','prefix','basic_family'].includes(component))return invalid('BAD_LOOKUP');
        const entry=lookup(brand,code,component);
        return json({entry,found:!!entry,status:entry?'OFFICIAL_CODE_ONLY':'NOT_FOUND',auto_replace_allowed:false});
      }
      if(req.method==='POST'&&path==='/v1/decode'){
        const o=await readSmallJSON(req);
        if(typeof o.brand!=='string'||o.brand.length>40||!safe(o.suffix,256))return invalid('BAD_DESIGNATION');
        return json(decode(o.brand,o.suffix));
      }
      if(req.method==='POST'&&path==='/v1/compare'){
        const o=await readSmallJSON(req);
        if(!o.left||!o.right||typeof o.left.brand!=='string'||typeof o.right.brand!=='string'
          ||!safe(o.left.suffix,256)||!safe(o.right.suffix,256))return invalid('BAD_PAIR');
        return json(compare(o.left,o.right));
      }
      if(path==='/v1/approve')return invalid('APPROVAL_ENDPOINT_NOT_AVAILABLE',403);
      return invalid('NOT_FOUND',404);
    }catch(e){
      if(['PAYLOAD_TOO_LARGE','JSON_ONLY','INVALID_JSON','OBJECT_REQUIRED'].includes(e?.message))
        return invalid(e.message,e.message==='PAYLOAD_TOO_LARGE'?413:400);
      return invalid('INTERNAL_ERROR',500);
    }
  }
};
).exec(value):/^(\d{3,7})(.*)$/.exec(value);
  if(!bodyMatch){issues.push('BASIC_DESIGNATION_UNRECOGNIZED');return {...empty(),brand,prefix,standard_hint};}
  const basic_designation=bodyMatch[1];
  const suffix=bodyMatch[2].trim();
  if(family && !VERIFIED_CODES.some(c=>c.manufacturer===brand && c.component==='basic_family' && c.code===family))
    issues.push('BASIC_FAMILY_NOT_OEM_VERIFIED');
  const decoded=decode(brand,suffix);
  if(suffix && decoded.status!=='VERIFIED_CODE_SCOPE_REVIEW')issues.push('UNVERIFIED_SUFFIX');
  if(/[А-ЯЁ]/u.test(basic_designation+suffix)&&/[A-Z]/u.test(basic_designation+suffix))issues.push('MIXED_ALPHABETS');
  return {raw_designation,brand,prefix,prefix_origin,basic_designation,suffix,standard_hint,
    source_codes:decoded.matched,unresolved_suffix_parts:decoded.unknown_parts,
    parse_status:issues.length?'REVIEW':'PARSED_COMPONENTS',issues,
    product_equivalence:'NOT_ASSESSED',auto_replace_allowed:false};
}

export default {
  async fetch(req){
    try{
      const url=new URL(req.url),path=url.pathname;
      if(req.method==='GET'&&path==='/health')
        return json({service:'EVEREST BearingsInfo',status:'ok',mode:'read-only',code_count:VERIFIED_CODES.length,approved_product_analogues:0});
      if(req.method==='GET'&&path==='/v1/lookup'){
        const brand=brandOf(url.searchParams.get('brand')),code=url.searchParams.get('code'),component=url.searchParams.get('component')||'suffix';
        if(!KNOWN_BRANDS.includes(brand)||!safe(code)||!['suffix','prefix','basic_family'].includes(component))return invalid('BAD_LOOKUP');
        const entry=lookup(brand,code,component);
        return json({entry,found:!!entry,status:entry?'OFFICIAL_CODE_ONLY':'NOT_FOUND',auto_replace_allowed:false});
      }
      if(req.method==='POST'&&path==='/v1/decode'){
        const o=await readSmallJSON(req);
        if(typeof o.brand!=='string'||o.brand.length>40||!safe(o.suffix,256))return invalid('BAD_DESIGNATION');
        return json(decode(o.brand,o.suffix));
      }
      if(req.method==='POST'&&path==='/v1/compare'){
        const o=await readSmallJSON(req);
        if(!o.left||!o.right||typeof o.left.brand!=='string'||typeof o.right.brand!=='string'
          ||!safe(o.left.suffix,256)||!safe(o.right.suffix,256))return invalid('BAD_PAIR');
        return json(compare(o.left,o.right));
      }
      if(path==='/v1/approve')return invalid('APPROVAL_ENDPOINT_NOT_AVAILABLE',403);
      return invalid('NOT_FOUND',404);
    }catch(e){
      if(['PAYLOAD_TOO_LARGE','JSON_ONLY','INVALID_JSON','OBJECT_REQUIRED'].includes(e?.message))
        return invalid(e.message,e.message==='PAYLOAD_TOO_LARGE'?413:400);
      return invalid('INTERNAL_ERROR',500);
    }
  }
};
