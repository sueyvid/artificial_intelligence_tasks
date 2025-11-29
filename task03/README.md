# Research Report
## Genetic Algorithms

### Technical Summary
Abstract: This study explores the application of Genetic Algorithms (GA) to solve a simplified version of the Knapsack Problem, an optimization challenge. The experiment involves creating an initial population of binary chromosomes, evaluating them via a Fitness Function, and applying evolutionary operators such as Selection, Crossover, and Mutation. The results demonstrate how evolutionary heuristics can iteratively improve a population of solutions to find an optimal or near-optimal configuration.

**Key Concepts**: Evolutionary Computing, Chromosomes, Fitness Function, Crossover, Mutation.

## Genetic Algorithm Application: Solving the Knapsack Problem
**Task Description**: Implement a manual iteration of a Genetic Algorithm to solve a simplified Knapsack Problem. The goal is to select the optimal combination of items to maximize value without exceeding a weight constraint.

### Technical Requirements:

1. Representation (Encoding):

    - Define a set of 4 items with specific weights and values.

    - Use Binary Encoding to represent individuals (chromosomes), where '1' implies the item is included and '0' implies it is excluded.

2. Initialization & Fitness:

    - Generate a random Initial Population of 4 individuals.

    - Calculate the Fitness Function for each individual (Sum of Values). Apply a penalty (fitness = 0) if the total weight exceeds the limit.

3. Evolutionary Operators:

    - Selection: Select the two best individuals as parents.

    - Crossover: Perform a one-point crossover operation to generate two offspring.

    - Mutation: Apply bit-flip mutation to one gene in the offspring to ensure diversity.

4. Report Deliverables:

    - Population Table: A table showing Genotypes, Phenotypes (items selected), and Fitness values.

    - Operator Analysis: A comparison of the population before and after the crossover/mutation steps.