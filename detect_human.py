import matplotlib; matplotlib.use('Agg')
import numpy as np
import os
import tensorflow as tf
from face_detect.Face_recognition import Face_recogn
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util

MODEL_NAME = 'model'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')



def benchmark(func):

    import time

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper

# def load_image_into_numpy_array(image):
#     (im_width, im_height) = image.size
#     return np.array(image.getdata()).reshape(
#         (im_height, im_width, 3)).astype(np.uint8)
def main_func():
    cap = cv2.VideoCapture(0)
    face_detect = Face_recogn()
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=90, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            while True:
                ret, image_np = cap.read()
                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                (boxes, scores, classes, num_detections) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                final_score = np.squeeze(scores)
                count = 0
                for i in range(100):
                    if scores is None or final_score[i] > 0.5:
                        count = count + 1
                #       print(count)
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8)
                image_np = face_detect.recogn_face(image_np)
                cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
if __name__ == "__main__":
    main_func()