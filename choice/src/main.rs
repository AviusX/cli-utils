use rand::{thread_rng, Rng};
use std::io::{self, Write};

fn read_int() -> i32 {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Error while reading input");
    input
        .trim()
        .parse()
        .expect("Error while parsing input into i32.")
}

fn read_choice() -> String {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Error while reading input.");
    input
}

fn random_choice(choices: &Vec<String>) -> &String {
    let mut rng = thread_rng();
    let random_index = rng.gen_range(0..choices.len());
    &choices[random_index]
}

fn main() {
    println!("AviusX's Choice Program");
    println!("_______________________");
    println!();
    print!("Enter the number of choices: ");
    io::stdout().flush().expect("Error while flushing stdout.");
    let num_choices = read_int();
    let mut choices: Vec<String> = Vec::new();

    for index in 0..num_choices {
        print!("Enter choice {}: ", index + 1);
        io::stdout().flush().expect("Error while flushing stdout.");
        let choice = read_choice();
        choices.push(choice);
    }

    let chosen_choice = random_choice(&choices);

    println!("The suggested choice is: {}", chosen_choice);
}
