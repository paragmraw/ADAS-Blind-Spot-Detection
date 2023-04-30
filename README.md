# ADAS Blind Spot Detection Using YOLOv8

The "ADAS Blind Spot Detection Using YOLOv8" project is a computer vision model that can identify safe and unsafe lane-changing conditions. The model uses the YOLOv8 algorithm from Ultralytics to detect objects and classify them into "safe" and "unsafe". It notifies the user via function calls and warning alarms if an "unsafe" class is detected i.e situations when changing lanes is dangerous.

Here are a few use cases for this project:

Assisting Autonomous Vehicles: This computer vision model can be integrated into self-driving cars to improve their safety during lane changes. The model's ability to identify safe and unsafe situations can help autonomous vehicles determine when it is safe to change lanes while avoiding accidents.

Driver Assistance Systems: The "Object Detection for Safe Lane Changing" can be used in Advanced Driver Assistance Systems (ADAS) to enhance safety for human drivers. The model can provide real-time alerts to the driver when it detects unsafe lane-changing conditions, allowing the driver to make more informed decisions and avoid potential accidents.

Road Safety Education: The computer vision model can be used as an educational tool for teaching drivers about safe lane-changing practices. Interactive simulations using this model can help new and experienced drivers understand the complexities of lane changes and identify potential hazards in various traffic scenarios.

Transportation Research: Researchers can utilize the "Object Detection for Safe Lane Changing" model to study traffic patterns, driver behavior, and accident-prone situations. By analyzing data from the model, researchers can develop new strategies to minimize the risk of accidents and improve overall road safety.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/paragmraw/ADAS-Blind-Spot-Detection.git
```

Go to the project directory

```bash
  cd ADAS-Blind-Spot-Detection
```
## Instructions:

1. Open the `train-val-pre.ipynb` notebook. If you don't have a GPU, you can ignore the first cell.

2. In cell 5 of the notebook, enter your Roboflow API key to use the annotated dataset in Roboflow. Alternatively, you can annotate your own dataset.
Note: Training your data is performed in this step. With an RTX 3060 + Intel i7 12th Gen configuration, it took around 7 minutes to train the model on YOLOv8.

3. Open the `visualization.ipynb` notebook to view the following:
   - Confusion_matrix
   - F1_curve
   - P_curve
   - PR_curve
   - R_curve
   - Results

4. Open the `main.ipynb` notebook. Select the specific video you want to use from the `SampleVideos` folder or use your own video if you have trained your custom dataset.

5. To set the playback speed change the value of "fr" variable. Lower fr -> Greater playback speed.

6. To quit the playback, press "q" repeatedly.

## Roboflow Link
- [Object Detection for Safe Lane Changing](https://universe.roboflow.com/dayananda-sagar-university-q7oox/object-detection-for-safe-lane-changing/model/1)

## Authors

- Parag Mandal: [LinkedIn](https://www.linkedin.com/in/paragmraw/) /
                [GitHub](https://github.com/paragmraw/)

## Acknowledgements

 - [Unannotated Data Source](https://gitlab.ika.rwth-aachen.de/cam2bev/cam2bev-data/)
 - [RWTH Aachen University](https://www.ika.rwth-aachen.de/en/)



