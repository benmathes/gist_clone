
## Gist clone:

#### Identify all of the user roles and actions (sometimes called “user stories”). What is it that users are able to do, and what should they expect to see as a result?

* one user type: user

actions:
* create text file
* commit changes to text file
* accept others' changes to the text file



#### Develop a “logical” model identifying the entities, relationships, attributes and invariants corresponding to the above, proceeding in roughly that order.

* User
* File: has many changes.
* Change (belongs to File, belongs to User)


#### Test the logical model against the user stories you defined. Will your model support all of the required functionality?

* create a text file:
  *

* Once you’re satisfied with your logical model, proceed to a “physical” model, ready to be implemented as a relational database. At this point, consider column types, foreign key constraints, primary key definitions (including composite keys if any), indexes, future performance concerns, and any other database-specific aspects.
