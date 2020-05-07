from pycocotools.coco import COCO
from cococt import COCOCT
import unittest


class COCOCTTest(unittest.TestCase):

    cococt = COCOCT("/data/Borneo/0.5/images.json")

    def test_has_loaded_something(self):
        self.assertGreater(len(self.cococt.locs), 0)
        self.assertGreater(len(self.cococt.seqs), 0)
        self.assertGreater(len(self.cococt.locToImgs), 0)
        self.assertGreater(len(self.cococt.seqToImgs), 0)
        self.assertGreater(len(self.cococt.locToSeqs), 0)


if __name__ == "__main__":
    unittest.main()
