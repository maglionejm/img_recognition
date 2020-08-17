#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='INSERT API KEY')

with open('/Users/juanmartinmaglione/Desktop/5678.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        classifier_ids=["default"]).get_result()
    print(json.dumps(classes, indent=2))


# In[ ]:




