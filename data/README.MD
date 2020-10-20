# Data folder Organization

```
external   <- Data from third party sources.
interim    <- Intermediate data that has been transformed.
processed  <- The final, canonical data sets for modeling.
raw        <- The original, immutable data dump.
```

# Notes:

- Data from labs 25 used as reference only. 

### Data sets inherited from Labs 25:

- police_use_force.csv 
    > A CSV with two columns. Col[name] is the name of a story. col[police_brutality] is irrelevant(never varies)

- news.csv  
    > A CSV with 1000 scraped news headlines.

# Labs 27:

## Use of Force Datasets

Sourced data from Police Data Initiative: [link](https://www.policedatainitiative.org/datasets/use-of-force/)

|  Name                      | City       | State  | Link                   | Title                     |  Type Processed 
|----------------------------|------------|--------|------------------------|---------------------------|

Austin Police Department       Austin         TX     https://goo.gl/jwylHu    Response to Resistance

Baltimore Police Department    Baltimore      MD     https://goo.gl/OvTBnP    Use of Force

Bedford Police Department      Bedford        VA     https://goo.gl/mJGYtC    Use of Force

Beloit Police Department       Beloit         WI     https://goo.gl/wgFYfO    Use of Force

Bloomington Police Department  Bloomington    IN     https://goo.gl/vKAazV    Use of Force

Cincinnati Police Department   Cincinnati     OH     https://goo.gl/JMxIxk    Use of Force

Dallas Police Department       Dallas         TX     https://goo.gl/51yKSa    Response to Resistance

Indianapolis PD                Indianapolis   IN     https://goo.gl/L5CWNt    Use of Force

Lincoln Department of PS       Lincoln        NE     https://goo.gl/4XupS6    Use of Control

New Orleans PD                 New Orleans    LA     https://goo.gl/1DC7sW    Use of Force

North Bergen PD                North Bergen   NJ     https://goo.gl/YT6mGF    Use of Force

Northampton PD                 Northampton    MA     https://goo.gl/G11zeX    Use of Force

Norwich PD                     Norwich        CT     https://goo.gl/abjESZ    Police Use of Force

Orlando PD                     Orlando        FL     https://goo.gl/0G9AqR    Response to Resistance

Portland PD                    Portland       OR     https://goo.gl/ubwvte    Use of Force

Seattle PD                     Seattle        WA     https://goo.gl/URK6rR    Use of Force

South Bend PD                  South Bend     IN     https://goo.gl/SieGqM    Police Use of Force Incidents

University of Delaware PD      Newark         DE     https://goo.gl/B2Rm6C    Use of Force


# Incident Information

- Date and time of the incident
- Total number of officers who applied actual force during the incident
- Number of officers from the reporting agency who applied actual force during the incident
- Location of the incident (address or latitude/longitude)
- Location type of the incident (street, business, residence, restaurant, school, etc.)
- Did the officer(s) approach the subject(s)?
- Was it an ambush incident?
- Was a supervisor or a senior officer acting in a supervisory capacity present or consulted at any point during the incident?
- What was the reason for initial contact between the subject and the officer (response to unlawful or suspicious activity, routine patrol, traffic stop, etc.)?
- If the initial contact was due to “unlawful or criminal activity,” what were the most serious reported offenses committed by the subject prior to or at the time of the incident?
- If applicable, the reporting agency will enter the National Incident-Based Reporting System or local incident number of the report detailing criminal incident information on the subject and/or assault or homicide of a law enforcement officer
- If the incident involved multiple law enforcement agencies, the agency will include case numbers for the local use-of-force reports at the other agencies

# Subject Information

- Age, sex, race, ethnicity, height, and weight
- Injury/death of subject(s) (gunshot wound, apparent broken bones, unconsciousness, etc.)
- Type(s) of force used connected to serious bodily injury or death (firearm, electronic control weapon, explosive device, blunt instrument, etc.)
- Did the subject(s) resist?
- Was the threat by the subject(s) directed to the officer or to another party?
- Type(s) of subject resistance/weapon involvement (threatened officer, threatened others, threatened self, active aggression, firearm, attempt to flee, etc.)
- Was there an apparent or known impairment in the physical condition of subject? If yes, indicate which (mental health/alcohol/drugs/unknown)
- At any time during the incident, was the subject(s) armed or believed to be armed with a weapon?

# Officer Information

- Age, sex, race, ethnicity, height, and weight
- Years of service as a law enforcement officer (total tenure, number of years)
- At the time of the incident, was the officer a full-time employee?
- Was the officer readily identifiable?
- Was the officer on duty at the time of the incident?
- Did the officer discharge a firearm?
- Was the officer injured?
- What was the officer’s injury type (gunshot wound, apparent broken bones, severe laceration, unconsciousness, etc.)


# Statistical data: 

```
{ "data": 
    [ "date" :
      "Incidents_number":
      "lat":
      "lon":
      "lethal":
      "Projectile":
      "Race_victim":
      "Race_police_officer":
      "Victim_gender":
      "police_officer_Gender":
                         ]
}
```

```                                   
{ 'ID' : {
    'incident_number'   : int
    'incident_date'     : dt
    'incident_location' : {'lat'   : int 
                           'lon'   : int 
                           'state' : str
                           'city'  : str }
    'subject_age'       : int
    'subject_sex'       : str
    'subject_eth'       : str
    'type_of_force':    : str
    'officer_age'       : int
    'officer_sex'       : str
    'officer_eth'       : str
}
```

Key code for Race:
==================
A- Asian/Pacific Island, Non-Hispanic
B- African American, Non-Hispanic
I- Indian/Alaskan Native, Non-Hispanic
K- African American, Hispanic
L- Caucasian, Hispanic
N- Indian/Alaskan Native, Hispanic
P- Asian/Pacific Island, Hispanic
U- Unknown
W- Caucasian, Non-Hispanic