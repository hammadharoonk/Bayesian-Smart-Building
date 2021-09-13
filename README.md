# Predictive Bayesian Network For Smart Building Scenario

## Background:

This BN describes the simple working operation of a smart building cooling and ventilation system in a tropical climate, during a time of a pandemic. A series of proximity sensors are placed inside an area where most of the time, few employees sit. However, 3 months of the year, there are busy deadline periods in which several employees from other branches or new seasonal hires may use the area and many more people may gather. 

Due to relative crowdedness, and the resulting higher temperatures due to body heat, or obvious danger of spreading illness, the building manager has programmed the system to note when a certain threshold of population percieved in the space is crossed. 

In that case, a signal is sent to actuators that would activate mechanical ventilation systems to pass in outside air at a higher rate, and increase removal of waste air.

Several occupants have requested that due to the pandemic, the system have manual controls, so they can increase the ventilation at will when they see more people around them, even if the sensor has not detected that the population threshold has been crossed, for whatever reason. However, due to the increased electricity cost that would be incurred, the manager has placed the manual control far away from the workspace to discourage constant manual overrides.

There is also the factor of human intervention, intentional or unintentional, which often causes false positives. Employees may inadvertently place objects in front of proximity sensors which cause the sensor to perceive the presence of extra occupants. Furthermore, some disgruntled occupants may place pieces of tape in front of sensors to accelerate the activation of sensors, which have to be removed by janitorial staff.

## Bayesian Network Graph
![alt text](https://github.com/hammadharoonk/bayesiansmartbuilding/blob/main/graph.jpg?raw=true)


## Usage
The BN can be used to:

1_track the usage of ventilation systems

2_analyze the timings and durations of periods of overcrowding

3_predict the chances of employees mishandling the sensors.

## Variables and BN Structure

**Variables:**

**Deadline Period (DP):** 3 non-consecutive months out of the year, the office experiences deadline periods in which several employees join the office temporarily to complete tasks. The unconditional probability of this being true is hence 3/12, or 25%.

**Overcrowding (O):** Past a certain occupancy threshold, more people sit in the office than is deemed safe by health experts. This is worrying to those in the office who are susceptible to viruses, as well as increasing the temperature due to body heat and increased computer equipment. Especially during the deadline period, there is a 70% chance of overcrowding, while otherwise there is a 10% of overcrowding due to impromptu meetings or guests.

**Human Intervention (HI):** As people learn more about the sensor system, some feel inclined to furtively block the proximity sensors to activate the ventilation system, not trusting the building manager. Furthermore, some people inadvertently may place their possessions, chairs, or potted plants against sensors, causing false positives and percepts. Since the janitorial staff makes sure to clean this up and keep the sensors clear, the unconditional probability of HI is only 15%.

**Sensors Activated (SA):** These are generally trustworthy pieces of equipment, but are unable to sense when they perceive a human, or an inadvertently placed object, or a deceptive piece of tape. In normal circumstances, they percieve overcrowding at varying distances, at a 90% probability, but with added human intervention and static objects placed on top, this increases to 95%. When there is no overcrowding, malicious employees may attempt to block the sensors, however due to the constant efforts of the janitorial staff, their attempts only succeed with a 70% chance.

**Manual Control (MC):** Employees may panic at seeing extra faces so they are given the option to manually override the system and switch on the ventilation... however, the manual override button is placed at the opposite end of the compound as a deterrence, so people only press it around 60% of the time when they see a lot of people, or only 20% when there is no overcrowding.

**Ventilators Activated (VA):** Conditioned on sensors (SA) and manual control (MC), the ventilation has an almost foolproof 99% chance of being switched on when both SA and MC are activated. This goes down to 90% with only sensors due to potential issues in wireless system, or 80% with only manual control (since the building manager may choose to disable the manual control if people use it too much). With no activation, it only has a very small 1% chance of being activated.


## Scenario 1)
**tracking the activation of ventilation systems based on evidence of no-deadline period, overcrowding, and a series of unactivated sensors, untouched manual control, and a combination of both:**

![alt text](https://github.com/hammadharoonk/bayesiansmartbuilding/blob/main/scenario_1.jpg?raw=true)

In 1A, we can see that even if the sensors are not activated due to possible technical fault, the employees will most probably switch on the manual control if they see overcrowding.

In 1B, we can see that the sensors will in all likelihood activate when overcrowding is perceived, in which case the manual control won't be necessary.

In 1C, we can see that if the sensors and manual control are both not activated, the ventilation system will not activate, as expected, since it is only conditioned on those two variables.

## Scenario 2)
**analyzing the timings and durations of periods of overcrowding:**

The BN may help to provide information about periods of overcrowding, based on energy data from the ventilation system. Using cameras in the building to ensure no tampering with the sensors, the evidence is given that there is no human intervention, and the evidence of prior ventilation system is usage can be gathered from energy data. The BN then shows that overcrowding is probable at those times.

![alt text](https://github.com/hammadharoonk/bayesiansmartbuilding/blob/main/scenario_2.jpg?raw=true)

## Scenario 3)
**predicting the chances of employees mishandling the sensors:**

The building manager observes that the ventilation system is activated, however it is not one of the deadline periods of the year. Checking into the system, they see that the manual override is also untouched. This leaves two possibilities: impromptu overcrowding that activated the sensors, or human intervention... Suspicious of the latter, they may input the evidence into the BN only to confirm their suspicions.

![alt text](https://github.com/hammadharoonk/bayesiansmartbuilding/blob/main/scenario_3.jpg?raw=true)


##Conditional Independencies

1) If overcrowding (O) is observed, this means that manual control (MC) is conditionally independent of deadline period (DP), since O being observed blocks the pat between DP and MC.

2) if Manual Control (MC) is observed, Overcrowding (O) is conditionally independent from Human Intervention (HI). MC blocks the path from O-MC-VA, so even though VA-SA-HI is active, the first triple is inactive which blocks the whole path.

3) If Sensors Activated (SA) and Manual Control (MC) are both observed, that means Ventilation Activated is conditionally independent from Overcrowding (O).

4) If Overcrowding (O) and Sensors Activated (SA) is observed, then Manual Control (MC) is conditionally independent from Human Intervention (HI).

5) With no evidence, Deadline Period (DP) and Human Intervention (HI) are conditionally independent, due to the V structure at SA and VA.
