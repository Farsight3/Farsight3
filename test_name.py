from scanner_handler import CheckQr


qr = [
    "19123",
    "133",
    "2445465",
    "1646"
]

scan_device = CheckQr()


def scan_bd(qr_check):
    if qr_check in qr:
        return True
    else:
        return None


scan_device.check_in_db = scan_bd

def test_check():
    for i in qr:
       try:
           scan_device.check_scanned_device(i)
           print("Сканування пройшло вдало")
       except ConnectionError:
           print("Стала похибка")



