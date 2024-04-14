from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
from .constant import Constant

constants = Constant()
imgLangHoa = constants.getLANGHOASADEC()
imgDaiHocCanTho = constants.getDAIHOCCANTHO()
imgBenNinhKieu = constants.getBENINHKIEU()
imgDenHung = constants.getDENHUNG()
imgChoNoi = constants.getCHONOI()

# HINH ANH
#1
class LangHoaSaDeImgcAction(Action):
    def name(self) -> Text:
        return "action_LangHoaSaDecImg"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hinhanh = []
        langHoaEntity = next(tracker.get_latest_entity_values('langHoa'), None)
        if langHoaEntity:
                for i in range(2):
                    img_number = random.randrange(len(imgLangHoa))
                    hinhanh.append(imgLangHoa[img_number])
                print("RANDOM NUMBER LA : ",img_number)
                
                dispatcher.utter_message(
                    text = f"{hinhanh[0]}"
                )
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi không có ảnh mà bạn yêu cầu.")
        return []
#2
class DaiHocCanThoImgAction(Action):
    def name(self) -> Text:
        return "action_DaiHocCanThoImg"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hinhanh = []
        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            for i in range(2):
                img_number = random.randrange(len(imgDaiHocCanTho))
                hinhanh.append(imgDaiHocCanTho[img_number])
            print("RANDOM NUMBER LA : ",img_number)
            
            dispatcher.utter_message(
                text = f"{hinhanh[0]}"
            )
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi không có ảnh mà bạn yêu cầu.")
        return []
#3
class BenNinhKieuImgAction(Action):
    def name(self) -> Text:
        return "action_BenNinhKieuImg"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hinhanh = []
        benninhkieuEntity = next(tracker.get_latest_entity_values('benninhkieu'), None)
        if benninhkieuEntity:
            for i in range(2):
                img_number = random.randrange(len(imgBenNinhKieu))
                hinhanh.append(imgBenNinhKieu[img_number])
            print("RANDOM NUMBER LA : ",img_number)
            
            dispatcher.utter_message(
                text = f"{hinhanh[0]}"
            )
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi không có ảnh mà bạn yêu cầu.")
        return []
#4
class ChoNoiImgAction(Action):
    def name(self) -> Text:
        return "action_ChoNoiCaiRangImg"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hinhanh = []
        chonoiEntity = next(tracker.get_latest_entity_values('chonoicairang'), None)
        if chonoiEntity:
            for i in range(2):
                img_number = random.randrange(len(imgChoNoi))
                hinhanh.append(imgChoNoi[img_number])
            print("RANDOM NUMBER LA : ",img_number)
            
            dispatcher.utter_message(
                text = f"{hinhanh[0]}"
            )
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi không có ảnh mà bạn yêu cầu.")
        return []
#5
class DenHungImgAction(Action):
    def name(self) -> Text:
        return "action_DenHungImg"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hinhanh = []
        chonoiEntity = next(tracker.get_latest_entity_values('chonoicairang'), None)
        if chonoiEntity:
            for i in range(2):
                img_number = random.randrange(len(imgDenHung))
                hinhanh.append(imgDenHung[img_number])
            print("RANDOM NUMBER LA : ",img_number)
            dispatcher.utter_message(
                text = f"{hinhanh[0]}"
            )
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi không có ảnh mà bạn yêu cầu.")
        return []
    
    ###############################

# DIA CHI
#1
class DaiHocCanThoAddressAction(Action):
    def name(self) -> Text:
        return "action_DaiHocCanThoAddress"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            dispatcher.utter_message(
                    text = f"https://s.net.vn/2Rvr"
                )
        else :
            dispatcher.utter_message(text=f"Rất tiếc tôi không thể tìm thấy địa điểm bạn yêu cầu.")
        return []
#2
class BenNinhKieuAddressAction(Action):
    def name(self) -> Text:
        return "action_BenNinhKieuAddress"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            dispatcher.utter_message(
                    text = f"https://s.net.vn/nvzu"
                )
        else :
            dispatcher.utter_message(text=f"Rất tiếc tôi không thể tìm thấy địa điểm bạn yêu cầu.")
        return []
#3
class LangHoaSaDecAddressAction(Action):
    def name(self) -> Text:
        return "action_LangHoaSaDecAddress"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            dispatcher.utter_message(
                    text = f"https://s.net.vn/JPLI"
                )
        else :
            dispatcher.utter_message(text=f"Rất tiếc tôi không thể tìm thấy địa điểm bạn yêu cầu.")
        return []

#4
class ChoNoiCaiRangAddressAction(Action):
    def name(self) -> Text:
        return "action_ChoNoiCaiRangAddress"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            dispatcher.utter_message(
                    text = f"https://s.net.vn/VwBy"
                )
        else :
            dispatcher.utter_message(text=f"Rất tiếc tôi không thể tìm thấy địa điểm bạn yêu cầu.")
        return []

#5
class DenHungAddressAction(Action):
    def name(self) -> Text:
        return "action_DenHungAddress"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ctuEntity = next(tracker.get_latest_entity_values('CanThoUn'), None)
        if ctuEntity:
            dispatcher.utter_message(
                    text = f"https://s.net.vn/YSY9"
                )
        else :
            dispatcher.utter_message(text=f"Rất tiếc tôi không thể tìm thấy địa điểm bạn yêu cầu.")
        return []
