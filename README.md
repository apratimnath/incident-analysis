# Incident Management

# Project Summary

### Requirement
Based on the organisation requirement, every day thousand of Incidents are registered on the ticketing tools, like Service Now, from which they are processed, assigned and closed.
Based on usecases we came up with analysis requirements in three specific areas of concern -

1. Predicting Priority of Tickets: so that we can take preventive measures or fix the problem before it surfaces.
2. Predict RFC (Request for change) and possible failure/misconfiguration of assets.
3. Forecast the incident volume iso that they can be better prepared with resources and technology planning.

### Dataset
The data for the analysis is taken from UCI Machine Learning Repository - http://archive.ics.uci.edu/ml/datasets/Incident+management+process+enriched+event+log

### Data Set Information:

This is an event log of an incident management process extracted from data gathered from the audit system of an instance of the ServiceNowTM platform used by an IT company. The event log is enriched with data loaded from a relational database underlying a corresponding process-aware information system. Information was anonymized for privacy.

Number of instances: 141,712 events (24,918 incidents)
Number of attributes: 36 attributes (1 case identifier, 1 state identifier, 32 descriptive attributes, 2 dependent variables)

### Attribute Information:

1. number: incident identifier (24,918 different values);
2. incident state: eight levels controlling the incident management process transitions from opening until closing the case;
3. active: boolean attribute that shows whether the record is active or closed/canceled;
4. reassignment_count: number of times the incident has the group or the support analysts changed;
5. reopen_count: number of times the incident resolution was rejected by the caller;
6. sys_mod_count: number of incident updates until that moment;
7. made_sla: boolean attribute that shows whether the incident exceeded the target SLA;
8. caller_id: identifier of the user affected;
9. opened_by: identifier of the user who reported the incident;
10. opened_at: incident user opening date and time;
11. sys_created_by: identifier of the user who registered the incident;
12. sys_created_at: incident system creation date and time;
13. sys_updated_by: identifier of the user who updated the incident and generated the current log record;
14. sys_updated_at: incident system update date and time;
15. contact_type: categorical attribute that shows by what means the incident was reported;
16. location: identifier of the location of the place affected;
17. category: first-level description of the affected service;
18. subcategory: second-level description of the affected service (related to the first level description, i.e., to category);
19. u_symptom: description of the user perception about service availability;
20. cmdb_ci: (confirmation item) identifier used to report the affected item (not mandatory);
21. impact: description of the impact caused by the incident (values: 1â€“High; 2â€“Medium; 3â€“Low);
22. urgency: description of the urgency informed by the user for the incident resolution (values: 1â€“High; 2â€“Medium; 3â€“Low);
23. priority: calculated by the system based on 'impact' and 'urgency';
24. assignment_group: identifier of the support group in charge of the incident;
25. assigned_to: identifier of the user in charge of the incident;
26. knowledge: boolean attribute that shows whether a knowledge base document was used to resolve the incident;
27. u_priority_confirmation: boolean attribute that shows whether the priority field has been double-checked;
28. notify: categorical attribute that shows whether notifications were generated for the incident;
29. problem_id: identifier of the problem associated with the incident;
30. rfc: (request for change) identifier of the change request associated with the incident;
31. vendor: identifier of the vendor in charge of the incident;
32. caused_by: identifier of the RFC responsible by the incident;
33. close_code: identifier of the resolution of the incident;
34. resolved_by: identifier of the user who resolved the incident;
35. resolved_at: incident user resolution date and time (dependent variable);
36. closed_at: incident user close date and time (dependent variable).


### Analysis
The data is ordinal, nominal as well as categorical. To analyze the data, various data processing techniques like Label Encoding and Standardization is used.
For training the data and predicting the target, algorithms used are - 

1. Support Vector Machine
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbor
5. ARIMA (Volume Forecasting)


### Priority Prediction - 
The factors used are - 

caller_id: identifier of the user affected;
opened_by: identifier of the user who reported the incident;
sys_created_by: identifier of the user who registered the incident;
contact_type: categorical attribute that shows by what means the incident was reported;
location: identifier of the location of the place affected;
category: first-level description of the affected service;
subcategory: second-level description of the affected service (related to the first level description, i.e., to category);
impact: description of the impact caused by the incident (values: High, Medium, Low);
urgency: description of the urgency informed by the user for the incident resolution (values: High, Medium, Low);
notify: categorical attribute that shows whether notifications were generated for the incident;

### RFC Prediction -
The factors used are - 

reassignment_count: number of times the incident has the group or the support analysts changed;
reopen_count: number of times the incident resolution was rejected by the caller;
sys_mod_count: number of incident updates until that moment;
made_sla: boolean attribute that shows whether the incident exceeded the target SLA;
category: first-level description of the affected service;
subcategory: second-level description of the affected service (related to the first level description, i.e., to category);
assignment_group: identifier of the support group in charge of the incident;
assigned_to: identifier of the user in charge of the incident;
problem_id: identifier of the problem associated with the incident;
priority: calculated by the system based on 'impact' and 'urgency';

### Volume Forecasting - 
ARIMA Model is for time-series prediction based on daily incident count

### Results
1. For predicting Ticket Priority, Random Forest gives almost 99.8% accuracy.
2. For predicting RFC, Random Forest gives almost 99.4% accuracy.
3. ARIMA Model (p,d,q = 5,1,0) predicts the incident volume for the next 7 days.
