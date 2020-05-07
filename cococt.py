import json
from pycocotools.coco import COCO


class COCOCT(COCO):
    def __init__(self, annotation_file):
        super(COCOCT, self).__init__(annotation_file)

        print("[pyCOCOCT] Building CameraTrap Indexes")

        self.locs = []
        self.seqs = []

        self.locToImgs = {}
        self.seqToImgs = {}
        self.locToSeqs = {}

        for img in self.dataset["images"]:

            if "location" in img:
                # create locs and locToImgs index
                if img["location"] not in self.locToImgs:
                    self.locs.append(img["location"])
                    self.locToImgs[img["location"]] = []
                    self.locToSeqs[img["location"]] = []

                    if "seq_id" in img:
                        self.locToSeqs[img["location"]].append(img["seq_id"])

                self.locToImgs[img["location"]].append(img)

            if "seq_id" in img:
                # create seqToImgs index
                if img["seq_id"] not in self.seqToImgs:
                    self.seqs.append(img["seq_id"])
                    self.seqToImgs[img["seq_id"]] = []

                self.seqToImgs[img["seq_id"]].append(img)

        print("[pyCOCOCT] Indexes Built")
