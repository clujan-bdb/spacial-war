from decimal import Decimal
from random import choice
from datetime import datetime
from typing import Union
from .decorators import caster


@caster(type=Decimal)
def replace_decimals(obj: any) -> Union[float, int, any]:
    return int(obj) if obj % 1 == 0 else float(obj)


@caster(type=float)
def replace_to_decimal(obj: any) -> Union[Decimal, any]:
    return Decimal(str(obj))


cast_datetime_to_isoformat = caster(type=datetime)(datetime.isoformat)


def planet_namer() -> str:
    prefixes = [
        "Zar", "Vor", "Xan", "Ald", "Bel", "Cor", "Dru", "El", "Fen", "Gar",
        "Hor", "Ith", "Jar", "Kor", "Lir", "Mar", "Nor", "Or", "Per", "Qor",
        "Ryn", "Syr", "Tor", "Uth", "Val", "Wor", "Xil", "Yar", "Zel", "New"
    ]
    suffixes = [
        "donia", "thar", "phos", "lorn", "cara", "nix", "tia", "bex", "dil",
        "mar", "nus", "ram", "ser", "tor", "vox", "xis", "yra", "zan", "cion",
        "dros", "goth", "hoth", "ith", "kros", "lyn", "mir", "noth", "por",
        "quor", "rith", " II", " III", " X", " Prime", " Major", " Minor"
    ]
    infixes = [
        "ar", "or", "ur", "al", "il", "an", "on", "el", "un", "in", "en", "ol",
        "ir", "ur", "ys", "us", "as", "os", "is", "es"
    ]
    prefix = choice(prefixes)
    infix = choice(infixes)
    suffix = choice(suffixes)
    planet_name = prefix + infix + suffix
    return planet_name
