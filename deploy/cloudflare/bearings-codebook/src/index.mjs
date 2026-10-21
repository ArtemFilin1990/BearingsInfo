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
  const body=await req.text();
  if(body.length>2048)throw Error('PAYLOAD_TOO_LARGE');
  let obj;try{obj=JSON.parse(body)}catch{throw Error('INVALID_JSON')}
  if(!obj||typeof obj!=='object'||Array.isArray(obj))throw Error('OBJECT_REQUIRED');
  return obj;
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
