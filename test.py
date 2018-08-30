from unittest import TestCase

from ner import ner


class TestNERBOT(TestCase):
    def test_nerbot_1(self):
        text = "Ngày 30/8, Công an huyện Ia Grai cho biết, trên địa bàn có việc một phụ nữ trẻ tên Nguyễn Thị Hường (" \
               "SN 1997, trú tại tổ dân phố 6, thị trấn Ia Kha, huyện Ia Grai) không có khả năng chi trả số tiền nợ " \
               "16 tỷ đồng "
        expected = ['<START:TIME> Ngày 30/8 <END>']
        actual = ner(text)
        self.assertEqual(expected, actual)

    def test_nerbot_2(self):
        text = "Chiều ngày 30/8, thông tin từ một cán bộ UBND thị trấn Vũ Quang (huyện Vũ Quang, Hà Tĩnh), một người " \
               "dân trên địa bàn đã phát hiện thi thể cháu Phạm Thị S. nổi dưới sông sau gần 2 ngày mất tích. "
        expected = ['<START:TIME> Chiều ngày 30/8 <END>',
                    '<START:LOC> huyện Vũ Quang , Hà Tĩnh ) <END>',
                    '<START:TIME> 2 ngày mất tích <END>']
        actual = ner(text)
        self.assertEqual(expected, actual)

    def test_nerbot_3(self):
        text = "Ngày 29/8, Sở Tài nguyên & Môi trường TP Đà Nẵng vừa có thông báo thu hồi 4 khu đất để xây dựng các " \
               "trạm dừng xe buýt ở các quận, huyện trên địa bàn thành phố. "
        expected = ['<START:TIME> Ngày 29/8 <END>']
        actual = ner(text)
        self.assertEqual(expected, actual)
