# PredictUSFlights - Flight Delay Prediction

PredictUSFlights is an innovative solution designed to tackle one of the most significant challenges in the aviation industry in the USA—flight delays. Delays not only affect customer satisfaction but also represent a considerable economic burden for airlines and impact the broader economy. By leveraging advanced predictive analytics, this project aims to transform raw data into actionable insights, enabling airlines to optimize operations, improve passenger experiences, and minimize unnecessary costs.

The significance of predicting flight delays extends beyond mere operational improvements; it's a strategic tool that can lead to a competitive advantage. As airlines strive to ensure punctuality, the ability to anticipate and mitigate potential delays can be a game-changer. For passengers, it translates to better travel planning and a more reliable journey. For airlines, it means enhanced resource management, reduced overheads from prolonged delays, and a more robust flight schedule.

Through the use of historical data, PredictUSFlights serves as a crucial decision-support tool for airline operators, airport authorities, and logistical planners across the United States. The economic implications of delay predictions are profound, ranging from saving millions in operational costs to bolstering the reliability of air transport as a means of connecting people and businesses across the country.

This project is for stakeholders in the aviation sector looking for a technical edge, data scientists interested in practical applications of machine learning, and software developers aiming to contribute to the next wave of travel technology. Join us in shaping the future of flight travel where on-time performance is not just a goal but a standard.

The model has an **accuracy of 66% and an area under curve of 0.72.**

This project is part of the Mid-term Project for [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)




## Run Locally

Pre-requisites

```bash
python
git
docker
```
Activate docker desktop

Clone the project

```bash
  git clone https://github.com/Haroldgio28/Airline-delay-prediction/tree/main
```

Go to the project directory

```bash
  cd my-project
```

Build the docker image

```bash
  docker build --no-cache  -t delay-project . 
```

Run the application using Docker

```bash
  docker run -it --rm -p 9696:9696 delay-project
```
For make a prediction about a specific flight, there are two ways:

1. Open the [notebook](https://github.com/Haroldgio28/Airline-delay-prediction/blob/main/notebooks/predict-test.ipynb) on Visual Studio Code or other code editor, and change the parameters.
2. In another command line, execute the [script](https://github.com/Haroldgio28/Airline-delay-prediction/blob/main/predict-test.py), changing the parameters on the script.


## Next Steps

- Deploy this solution to a cloud (AWS)
- Iterate with XGBoost Classifier Model 

## Appendix

### Above the data
The dataset used in this project comprises 539,383 records of flights within the United States, each with 8 distinct features. It has been sourced from [Kaggle](https://www.kaggle.com/datasets/jimschacko/airlines-dataset-to-predict-a-delay/data).

For change values in the predict script, please take note of following abbreviations for airline and airport

#### Airline abbreviations 
Please note: the airline abbreviations should be in lower case.
- Alaska Airlines AS / asa
- American Airlines AA/aal
- Air Canada AC/aca
- Aeromexico AM / amx
- Continental Airlines CO / coa
- Delta Airlines DL / dal
- FedEx FX / fdx
- Hawaiian Airlines HA / hal
- Northwest Airlines NW / nwa
- Polar Air Cargo PO / pac
- Southwest Airlines SW / swa
- United Airlines UA / ual
- United Parcel (UPS) 5X / ups
- Virgin Atlantic VS / vir
- VivaAerobús VB / viv
- WestJet WS / wj

#### Airport abbreviations 
Please note: the airport abbreviations should be in lower case.
- atl - Hartsfield-Jackson Atlanta International Airport - Georgia
- aus - Austin-Bergstrom International Airport - Texas
- bna - Nashville International Airport - Tennessee
- bos - Boston Logan International Airport - Massachusetts
- bwi - Baltimore-Washington International Thurgood Marshall Airport - Washington
- clt - Charlotte Douglas International Airport - North Carolina
- dal - Dallas Love Field - Texas
- dca - Ronald Reagan Washington National Airport - Arlington, Virginia
- den - Denver International Airport - Colorado
- dfw - Dallas/Fort Worth International Airport - Texas
- dtw - Detroit Metropolitan Airport - Michigan
- ewr - Newark Liberty International Airport - New Jersey
- fll - Fort Lauderdale–Hollywood International Airport - Florida
- hnl - Daniel K. Inouye International Airport - Honolulu, Hawaii
- hou - William P. Hobby Airport - Houston, Texas
- iad - Dulles International Airport - Virginia
- iah - George Bush Intercontinental Airport - Houston, Texas
- jfk - John F. Kennedy International Airport - Queens, New York
- las - McCarran International Airport - Las Vegas, Nevada
- lax - Los Angeles International Airport - California
- lga - LaGuardia Airport - Queens, New York
- mco - Orlando International Airport - Florida
- mdw - Chicago Midway International Airport - Illinois
- mia - Miami International Airport - Florida
- msp - Minneapolis–Saint Paul International Airport - Minnesota
- msy - Louis Armstrong New Orleans International Airport - Louisiana
- oak - Oakland International Airport - California
- ord - O'Hare International Airport - Chicago, Illinois
- pdx - Portland International Airport - Oregon
- phl - Philadelphia International Airport - Pennsylvania
- phx - Phoenix Sky Harbor International Airport - Arizona
- rdu - Raleigh-Durham International Airport - North Carolina
- san - San Diego International Airport - California
- sea - Seattle–Tacoma International Airport - Washington
- sfo - San Francisco International Airport - California
- sjc - Norman Y. Mineta San Jose International Airport - California
- slc - Salt Lake City International Airport - Utah
- smf - Sacramento International Airport - California
- stl - St. Louis Lambert International Airport - Missouri
- tpa - Tampa International Airport - Florida

#### Day of week
Should be a number between 1 and 7 where 1 is sunday, 2 is monday and so on.

#### Time
Departure time measured in minutes from midnight (range 10-1439)

#### Length 
Duration of the flight in minutes




## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Haroldgio28)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haroldgiovannyuribe/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/HaroldGio28)
