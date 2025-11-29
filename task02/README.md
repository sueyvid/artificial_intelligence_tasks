# Research Report
## Fuzzy Logic

### Technical Summary
Abstract: This project simulates a Fuzzy Logic Inference System designed to determine the appropriate tip amount based on service and food quality inputs. The methodology follows the Mamdani inference process, involving three key stages: Fuzzification of crisp inputs using membership functions, Application of fuzzy rules, and Defuzzification using the Centroid method to generate a precise output. The report illustrates how fuzzy logic handles vague concepts and uncertainty in decision-making.

**Key Concepts**: Fuzzification, Membership Functions, Fuzzy Rules, Defuzzification (Centroid).

## Fuzzy Logic Controller: Service Tipping System Simulation
**Task Description**: Design and simulate a Fuzzy Logic Controller (Mamdani type) to determine the tip amount for a service based on two input variables: Food Quality and Service Quality.

### Technical Requirements:

1. Variable Definition:

    - Define Input Variables: Food Quality (e.g., Bad, Good, Delicious) and Service Quality (e.g., Poor, Average, Excellent).

    - Define Output Variable: Tip Amount (e.g., Low, Medium, High).

2. Fuzzification:

    - Design Membership Functions (triangular or trapezoidal) for each linguistic term of the variables.

    - Assign a scale (e.g., 0 to 10) for the inputs and map specific crisp values (e.g., Food=3, Service=8) to their respective fuzzy degrees.

3. Rule Evaluation & Aggregation:

    - Create a Rule Base (e.g., "IF Food is Bad OR Service is Poor THEN Tip is Low").

    - Apply fuzzy operators (MAX for OR, MIN for AND) to determine the firing strength of each rule.

4. Report Deliverables:

    - Graphical Representation: Sketches of the membership functions.

    - Fuzzy Calculation: The mathematical steps showing the fuzzification and rule application.

    - Output Visualization: A visual representation of the aggregated area for Defuzzification (Centroid concept).