# Notes about function



## Simple fn definitions 

### key points

1. We have two stages for functions.  **Declaring** and **calling** them.
2. When you declare them you determine the **parameters** (noted as a token with a lexeme). When you call it you bind them to evaluated **arguments**. For instance `add(a, b, c)` would have `a`, `b` and `c` as the arguments. 
3. When we ***call*** a function or other ***declared*** values we're creating a new environment. It essentially tells us that we're in a new scope.
   1. New scopes can bind their own arguments.
   2. That way when you can run the function environment and simply see where they exist (or if they do).


### Variable & Environment Management

Dynamically set environments.

![Binding Diagram](./images/binding.png)

Bind variables to an environment.

![Binding Diagram](./images/env_bind.png)

## Closures - Why They're Necessary

### Key points

The logic is for something like this.

```js
fun makeCounter() {
  var i = 0;
  fun count() {
    i = i + 1;
    print i;
  }

  return count;
}

var counter = makeCounter();
counter(); // "1".
counter(); // "2".

```

This presents issues:

1. The parent function is global. 
2. If the top (or any level) of function higher than `makeCounter` won't know to reference `makeCounter` variables.
3. The variable won't be trackable.
4. 