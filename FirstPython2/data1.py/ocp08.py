##개방폐쇄원칙(OCP)위반:준수하지 않는 VideoPlayer 클래스
# class VideoPlayer:
#     def __init__(self, format_type):
#         self.format_type = format_type

#     def start(self):
#         if self.format_type == "MP4":
#             self.play_mp4()
#         elif self.format_type == "WMV":
#             self.play_wmv()
#         elif self.format_type == "AVI":
#             self.play_avi()
#         elif self.format_type == "MP21":
#             self.play_mp21()
#         else:
#             print("지원하지 않는 형식입니다.")

#     def play_mp4(self):
#         print("MP4 비디오 재생중...")
#     def play_wmv(self):
#         print("WMV 비디오 재생중...")
#     def play_avi(self):
#         print("AVI 비디오 재생중...")
#     def play_mp21(self):
#         print("MP21 비디오 재생중...")

# #실행예시
# if __name__ == "__main__":
#     player = VideoPlayer("MP4")
#     player.start()

#     player = VideoPlayer("WMV")
#     player.start()

#     player = VideoPlayer("AVI")
#     player.start()

#     player = VideoPlayer("MP21")
#     player.start()

#     player = VideoPlayer("MKV")
#     player.start()

# ##개방폐쇄원칙(OCP)준수

##LSP 리스코프교체원칙(위반)

# class Lecturer:
#     def  __init__(self):
#         self.lecturer ="일반강사"
#         self.charge = 90000

#     def display_info(self):
#         print(self.lecturer)
#         print(f"강사료: {self.charge}원\n")

# class LecturerNight(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="야간강사"
#     def display_info_night(self):
#         print(self.lecturer)
#         print(f"강사료: {self.charge *1.5}원\n")

# class LecturerAtGS(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="대학원강사"
   
#     def display_info_night(self):
#         print(self.lecturer)
#         print(f"강사료: {self.charge *2}원\n")

# class LecturerWithWork(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="직업이 있는 강사"
#     def display_info_night(self):
#         print(self.lecturer)
#         print(f"일일 주차비: {self.charge * 0.5}원\n")
        
# if __name__ =="__main__":
#     lect = Lecturer()
#     lect.display_info()

#     lect01 = LecturerAtGS()
#     lect01.display_info()

#     lect02 = LecturerNight()
#     lect02.display_info()

#     lect03 = LecturerWithWork()
#     lect03.display_info()


    ##LSP 리스코프교체원칙(준수)

# from abc import ABC, abstractmethod

# class  Lecturer(ABC):
#     def __init__(self):
#         self.lecturer = ""
#         self.charge = 90000

#     @abstractmethod
#     def display_info(self):
#         pass

# class GeneralLecturer(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="일반강사"

#     def display_info(self):
#          print(self.lecturer)
#          print(f"강사료: {self.charge}원\n")

# class LecturerNight(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="야간 강사"
        
#     def display_info(self):
#          print(self.lecturer)
#          print(f"강사료: {self.charge*1.5}원\n")

# class LecturerAtGS(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="대학원 강사"
        
#     def display_info(self):
#          print(self.lecturer)
#          print(f"강사료: {self.charge*2}원\n")

# class LecturerWithWork(Lecturer):
#     def  __init__(self):
#         super().__init__()
#         self.lecturer ="직업이 있는 강사"
        
#     def display_info(self):
#          print(self.lecturer)
#          print(f"강사료: {self.charge*0.5}원\n")

# if __name__ =="__main__":
#     lect = GeneralLecturer()
#     lect.display_info()

#     lect01 = LecturerAtGS()
#     lect01.display_info()

#     lect02 = LecturerNight()
#     lect02.display_info()

#     lect03 = LecturerWithWork()
#     lect03.display_info()

# ## 인터페이스 분리원칙(위반)

# class MultiFunctionDevice:
#     def print(self):
#         pass
#     def scan(self):
#         pass
#     def fax(self):
#         pass

# class SmartPrinter(MultiFunctionDevice):
#     def print(self):
#         print("문서 인쇄 중...")
#     def scan(self):
#         print("문서 스캔 중...")
#     def fax(self):
#         print("팩스 전송 중...")

# class BasicPrinter(MultiFunctionDevice):
#     def print(self):
#         print("문서 인쇄 중...")
#     def scan(self):
#         raise NotImplementedError("스캔 기능을 지원하지 않습니다.")
#     def fax(self):
#         print("팩스 기능을 지원하지 않습니다.")

# if __name__ =="__main__":
#     printer = SmartPrinter()
#     printer.print()
#     printer.scan()
#     printer.fax()

#     basic_printer = BasicPrinter()
#     basic_printer.print()

## 인터페이스 분리원칙(준수)
class Printer:
    def print(self):
        pass

class ScannerFax:
    def scan(self):
        pass
    def fax(self):
        pass

class SmartPrinter(Printer, ScannerFax):
    def print(self):
        print("문서 인쇄 중...")
    def scan(self):
        print("문서 스캔 중...")
    def fax(self):
        print("팩스 전송 중...")

class BasicPrinter(Printer):
    def print(self):
        print("문서 인쇄 중...")


if __name__ =="__main__":
    printer = SmartPrinter()
    printer.print()
    printer.scan()
    printer.fax()

    basic_printer = BasicPrinter()
    basic_printer.print()

