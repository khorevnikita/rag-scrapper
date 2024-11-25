from sources.eat_right.scrapper import EatRightLinkCollector, EatRightTextExtractor
from sources.mayo_clinic_health_system.scrapper import MayoClinicTextExtractor, MayoClinicLinkCollector
from sources.eufic.scrapper import EuFicTextExtractor, EuFicLinkCollector
from interfaces import LinkCollector, TextExtractor


def get_scrapper(key: str) -> (LinkCollector | None, TextExtractor | None):
    class_map = {
        "eat_right": (EatRightLinkCollector, EatRightTextExtractor),
        "mayo_clinic_health_system": (MayoClinicLinkCollector, MayoClinicTextExtractor),
        "eufic": (EuFicLinkCollector, EuFicTextExtractor)
    }

    if key not in class_map:
        return None, None

    return class_map[key]
