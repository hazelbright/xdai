//This script-file contains the essentials in order to be able to drive xdai

function createObject(object, variableName){
    //Bind a variable whose name is the string variableName
    // to the object called 'object'
    // To run this you:
    // import js
    // from pyodide import create_proxy
    // and run this line to create an accessible js object: js.createObject(create_proxy(nameInPython), "newNameInJs")
    let execString = variableName + " = object"
    console.log("Running `" + execString + "`");
    eval(execString)
}