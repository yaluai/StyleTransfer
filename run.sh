#!/usr/bin/env bash
python2 tools/infer_simple.py \
    --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml \
    --output-dir output1/ \
    --image-ext jpg \
    --wts https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    demo
python imageEdit.py
python3s style_transfer/Style-Transfer.py
mv *.jpg demo/output3/
python imageEdit2.py
