_base_ = [
    '../_base_/obj/models/pspnet_r50-d8.py',
    '../_base_/obj/datasets/pascal_voc12_aug.py', '../_base_/obj/default_runtime.py',
    '../_base_/obj/schedules/schedule_20k.py'
]
model = dict(
    decode_head=dict(num_classes=4), auxiliary_head=dict(num_classes=4))
