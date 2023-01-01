function greetUser(){
    console.log("Bom dia");
    console.log("Bem vind@");
}

greetUser();

function greet(name){
    console.log("Olá, "+ name);
}
greet("Adriano");
greet("Fulan@");

let number = 300;

function mostrarMetade (numero){
    console.log("A metade de " + numero + " é:");
    const metade = numero / 2;
    console.log(metade);
}

mostrarMetade(number);

function mostrarDobro (numero){
    console.log("O dobro de " + numero + " é:");
    const dobro = numero * 2;
    console.log(dobro);
}

mostrarDobro (number);

function idadeUsuario(idade){
    const iu = "Idade: " + idade;
    return iu;
}

const idade = idadeUsuario(30);
console.log(idade);

function display(primeiro, segundo, terceiro){
    return primeiro + segundo + terceiro;
}

const result = display("1o.", "2o.", "3o.");
console.log(result);

function somaTotal(preco, imposto){
    console.log("Preço: " + preco + ". Imposto: " + imposto + ".")
    console.log("Total:")
    console.log(preco + imposto);
}
somaTotal(1000, 320);

function isFreezing(temperatura){
    return temperatura < 0;
}
const congelando = isFreezing(-1);
console.log("Temperatura de congelamento?")
console.log(congelando);
