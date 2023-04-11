Segment anything proto notes 


```bash
mkdir assets 
wget -q https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth > null
wget -q https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth > null
wget -q https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth > null
wget https://fastly.picsum.photos/id/1/5000/3333.jpg?hmac=Asv2DU3rA_5D1xSe22xZK47WEAN0wjWeFOhzd13ujW4
pip install opencv-python pycocotools matplotlib onnxruntime onnx
```


```python 
def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    polygons = []
    color = []
    for ann in sorted_anns:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for i in range(3):
            img[:,:,i] = color_mask[i]
        ax.imshow(np.dstack((img, m*0.35)))
```



### Get some random images 


```bash
wget -q -O unsplash_wallpaper.jpg https://unsplash.it/400/400/?random
wget -q -O house.jpeg https://a.allegroimg.com/original/127215/a053eba446eda7b599b06ba170d1
```


### Inference snippet
Model size independent 



```
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from segment_anything import SamAutomaticMaskGenerator
mask_generator = SamAutomaticMaskGenerator(build_sam(checkpoint = "assets/sam_vit_h_4b8939.pth"))
masks = mask_generator.generate(image)

image = Image.open("house.jpg")
image = np.array(image)

masks = mask_generator.generate(image)
```
