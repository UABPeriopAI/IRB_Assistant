CONTRACT = """# Pre-submission checklist

This draft was created by a generative artificial intelligence (AI).

We hope that its assistance saved you time. However, it is only intended as a rough draft.
As with any AI-generated text, _you_ are ultimately responsible for the content of the final document.

To reduce the need for back-and-forth communication with the Research team and the IRB, complete the following checklist.


- [ ] Add PI and CO-I names.
- [ ] Add Coordinator, Assistant, and/or resident names(s) as applicable.
- [ ] Confirm all investigators are current with IRB and GCP training.
- [ ] Confirm the list of variables to be collected is **exhaustive** for your study. Changing this later may require IRB ammendments or resubmission (i.e., repeating the process).
- [ ] Add sample-size information (including any study groupings) as appropriate. The department statistician, research team, or data science team can help you with this step.
- [ ] Add a study budget to the resources section if applicable. This step is required for sample analysis, pharmacy costs, any patient payments, grants, contracts, or agreements with an existing or planned funding source.
- [ ] Note in the Resources section if you want assistance adding your study to [clinicaltrials.gov](https://clinicaltrials.gov/).
- [ ] Review and edit all sections.
- [ ] **Unique to the study-type you selected:**

"""

FRONT_MATTER = """***Department of Anesthesiology Clinical Research Protocol***

**Principal Investigator\*:**

**Co-Investigators (indicate department)\*:**

**Research Coordinator/Assistant\*:** *Enter text here if applicable*

**Resident\*:**

*\*Must have completed / be current with IRB & GCP training requirements -- otherwise the IRB will not approve your protocol\*.*

**Version Date:** *Enter text here if applicable*

**IRB Study Number:** *Enter text here if applicable* (pending)

***INDEX***

| Content | Section |
| --- | --- |
| Summary of Study | 1|
| Background & Rationale | 2 |
| Objective(s) & Hypothesis | 3 |
| Inclusion & Exclusion Criteria | 4 |
| Randomization Procedures | 5 |
| Study Interventions/Procedures | 6|
| Plan for Study | 7 |
| Statistical Considerations | 8 |
| Adverse Event Reporting | 9 |
| Study Budget and Resources | 10 |
| References | 11 |
| Drug and Device Information | 12 |
| Patient Safety & Data Security Monitoring | 13 |

---"""

BACK_MATTER = """

# Drug and Device 

## Drug Information (if applicable)

Drug Name: *Enter text here if applicable*

Other Names: *Enter text here if applicable*

Classification: *Enter text here if applicable*

Mode of Action: *Enter text here if applicable*

Storage and Stability: *Enter text here if applicable*

Metabolism: *Enter text here if applicable*

Preparation: *Enter text here if applicable*

Administration: *Enter text here if applicable*

*Incompatibilities:* *Enter text here if applicable*

-   *Contraindications:* *Enter text here if applicable*

-   *Precautions:* *Enter text here if applicable*

*Enter text here if applicable*

**Side Effects:** Adverse effects indicated in *italics* are the most frequent adverse effects. Adverse events in bold are severe/life-threatening, otherwise they are mild to moderate in reaction.

CNS: *Enter text here if applicable*

CV: *Enter text here if applicable*

EENT: *Enter text here if applicable*

ENDO: *Enter text here if applicable*

GI: *Enter text here if applicable*

GU: *Enter text here if applicable*

INTEG: *Enter text here if applicable*

MS: *Enter text here if applicable*

Investigational New Drug (IND) Application required (check yes or no): [ ] Yes [ ] No

Will the research Pharmacy be involved in the ordering, storage, dispensing and blind of the study drug? [ ]  Yes [ ]  No

## Device Information (if applicable)

Device Name: *Enter text here if applicable* Other Names: *Enter text here if applicable*

Classification: *Enter text here if applicable*

Mechanism of Action: *Enter text here if applicable*

Medication(s) Delivered: *Enter text here if applicable*

Incompatibilities: *Enter text here if applicable*

*Contraindications*: *Enter text here if applicable*

*Precautions*: *Enter text here if applicable*

***SIDE EFFECTS:*** Adverse effects indicated in *italics* are the most frequent adverse effects. Adverse events in **bold** are severe/life-threatening, otherwise they are mild to moderate in reaction.

CNS: *Enter text here if applicable*

CV: *Enter text here if applicable*

EENT: *Enter text here if applicable*

ENDO: *Enter text here if applicable*

GI: *Enter text here if applicable*

GU: *Enter text here if applicable*

INTEG: *Enter text here if applicable*

MS: *Enter text here if applicable*

Investigational Device Exemption (IDE) required check yes or no): [ ] Yes [ ] No (If yes, provide details. *Enter text here if applicable*



# Patient Safety and Data Security Monitoring

-   Assessment of Level of Risk: [ ] High [ ] Medium [ ] Low [ ] Not applicable

*Enter text here if applicable*

-   Reporting adverse events:

**The following is standard language that may be useful to include in your protocol.**

The personnel listed on the protocol and our research personnel will adhere to HIPAA guidelines to protect patient privacy and confidentiality. In order to protect the privacy interests of the participants, patient’s protected health information will be de-identified. We will extract data from electronic medical records, including intraoperative records. Irrespective of source, all data will be de‐identified. Data collected during the course of the project will only be accessible by the primary investigator, the co-investigators, and members of the research team. During data collection, all patient identifiers will be protected by the investigator, and at the completion of data collection, all of the results will be presented without patient identifiers. Only the PI, co-investigators, and other IRB-approved study personnel will have access to PHI. All files will be stored in password-protected computers in locked offices at UAB and in the RedCap system. Access to these particular systems is restricted to only IRB-approved members of the research team. All approved data elements, including patient identifying information, will be downloaded into a study specific dataset that is stored on a HIPAA compliant, encrypted, password-protected, central server that exists behind the hospital firewall. The server is maintained for Human Subjects Research by the UAB Department of Anesthesiology and Perioperative Medicine. All data will be de-identified and access to key linking access to the patient identifying information restricted to the PI and/or team members who have been specifically approved for access to the overall data set. For all data analysis, only de-identified datasets will be used.

"""
