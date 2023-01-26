# Work in progress!!!
# jdtree
Json Based DMN Rule Engine.
The purpose of this library is to parse a decision tree/table 
created with [jdtree-ui](https://github.com/mattskinosix/jdtree-ui)
And give you the result node based on input attributes 


## Multithreading 

All roots start a new thread


## Example

Given this json

if the input is temperatura = 9 then the output was COLD 

if the input is temperatura = 11 then the output was HOT 

      {
         "root":{
            "variableType":"number",
            "variableName":"temperatura",
            "leafs":[
               {
                  "id":"f7dff1c4-08ea-424e-90b2-a002053ac651",
                  "value":"10",
                  "operator":">",
                  "leafs":[
                     {
                        "result":{
                           "ciao":"HOT"
                        }
                     }
                  ]
               },
               {
                  "id":"34646224-ba40-40e3-a553-ffaca0e35d16",
                  "value":"10",
                  "operator":"<",
                  "leafs":[
                     {
                        "result":{
                           "ciao":"COLD"
                        }
                     }
                  ]
               }
            ]
         }
      }



 
