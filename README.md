<h1 align="center"> Cultural classifier </h1>

Cultural classifier is an application using the ML model to distinguish between two archaeological cultures (specifically epigravettian and epiaurignacian) that are hard to classify with the conventional classification approach that relies on analysing the stone tool industry.<br>

* machine learning for classification purposes in archaeology
* practical usage of the XGBoost  model as a complement for classifying stone industry, trained model and all data are available [here](https://github.com/hampet1/arch_data_analysis_and_model_for_cultural_classifier)
* all archaeological sites are represented by using interactive maps

## Watch the video about cultural classifier or checkout the app

<h4>Watch the video <a href="https://trackmood.herokuapp.com">here</a></h4>
<h4>You can checkout the app <a href="https://cultural-classifier.herokuapp.com/">here</a></h4>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

  ```sh
  pip (package manager)
  python 3.6 (and newer versions)
  ```

### Installation


1. Clone the repo
   ```
   git clone https://github.com/hampet1/moodtracker.git
   ```
2. Install packages
   ```
   pip install -r requirements.txt
   ```
3. Set up config
   ```
   * set FLASK_ENV=development
   * set FLASK_APP=main
   ```
4. Run server
   ```
   flask run
   ```  

<!-- USAGE EXAMPLES -->
## Usage

Classifier distinguishes between two very simalar archaeological cultures in terms of material culture. The input data (attributes) includes 
geospacial data related to the archaeological sites, the output is one of the archaeological cultures.
For more information regarding input data please checkout the [guideline](https://cultural-classifier.herokuapp.com/guideline).

For more info please checkout the website [about project](https://cultural-classifier.herokuapp.com/about-project)

## More resources

The scientific paper which backs up the whole idea of applyingthe  machine learning model for classification purposes in such fields as archeology is available [here](https://www.sciencedirect.com/science/article/abs/pii/S1040618220303657)  

## Known issues (work in progress)

It's absolutely crucial to collect more data regarding these archaeologically hard to determine cultures in order to fully understand the potential of this quite
new approach. At this stage the amount of data is not sufficient, that's why we should take this project for the time being with a grain of salt. 

## Acknowledgment

All data was collected by associate professors [Zdenka Neruda](https://www.researchgate.net/scientific-contributions/Zdenka-Nerudova-51407602) and 
[Petr Neruda](https://www.researchgate.net/profile/Petr-Neruda), under the patronage of the [Anthropos Institute](http://www.mzm.cz/en/anthropos-pavilion/).  

<!-- LICENSE -->
## License

Distributed under the MIT License.


<!-- CONTACT -->
## Contact

Petr Hamrozi - hamrozipetr@outlook.com








