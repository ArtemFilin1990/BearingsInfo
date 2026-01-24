"""
Модели данных (Pydantic schemas).

Определяет структуры данных для:
- Подшипников
- Аналогов
- Стандартов
- Производителей
"""

from datetime import datetime

from pydantic import BaseModel, Field

# Placeholder для кода из bearing-api/app/models.py


class BearingBase(BaseModel):
    """Базовая модель подшипника"""

    designation: str = Field(..., description="Обозначение подшипника")
    bearing_type: str | None = Field(None, description="Тип подшипника")
    inner_diameter: float | None = Field(None, description="Внутренний диаметр (d), мм")
    outer_diameter: float | None = Field(None, description="Наружный диаметр (D), мм")
    width: float | None = Field(None, description="Ширина (B), мм")


class Bearing(BearingBase):
    """Полная модель подшипника"""

    id: int
    manufacturer: str | None = None
    standard: str | None = None
    dynamic_capacity: float | None = None
    static_capacity: float | None = None
    created_at: datetime | None = None

    class Config:
        from_attributes = True


class BearingCreate(BearingBase):
    """Модель для создания подшипника"""

    pass


class Analog(BaseModel):
    """Модель аналога подшипника"""

    original_designation: str
    analog_designation: str
    manufacturer: str | None = None
    standard: str | None = None
    compatibility: float | None = Field(None, description="Степень совместимости (0-1)")


class SearchParams(BaseModel):
    """Параметры поиска подшипников"""

    designation: str | None = None
    bearing_type: str | None = None
    min_inner_diameter: float | None = None
    max_inner_diameter: float | None = None
    min_outer_diameter: float | None = None
    max_outer_diameter: float | None = None
    manufacturer: str | None = None
    standard: str | None = None
    limit: int = Field(100, ge=1, le=1000)
    offset: int = Field(0, ge=0)
