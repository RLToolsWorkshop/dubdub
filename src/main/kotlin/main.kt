class HelloName(name: String){
    private var name = name;
    fun logTo(){
        println("Hello ${name?.capitalize()}")
    }
}

fun main(args: Array<String>) {
    println("What is your name?")

    val name: String = readLine().toString();
    val helloName = HelloName(name);
    helloName.logTo();
}