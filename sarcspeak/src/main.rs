use copypasta_ext::prelude::*;
use copypasta_ext::x11_bin::ClipboardContext;
use std::env;

fn main() {
    let mut input_string = String::new();
    const ALPHABET: &str = "abcdefghijklmnopqrstuvwxyz";

    for arg in env::args().skip(1) {
        input_string.push_str(&arg);
        input_string.push(' ');
    }

    input_string = input_string.trim().to_lowercase();
    let mut output_string = String::new();
    let mut upper = true;

    for letter in input_string.chars() {
        if letter != ' ' && ALPHABET.contains(letter) && upper {
            output_string.push(letter.to_ascii_uppercase());
            upper = false;
        } else if letter != ' ' && ALPHABET.contains(letter) {
            output_string.push(letter);
            upper = true;
        } else {
            output_string.push(letter);
        }
    }

    let mut ctx = ClipboardContext::new().expect("Error while getting clipboard context.");
    ctx.set_contents(output_string).expect("Error while setting clipboard contents.");
    println!("Sarctext successfully copied to clipboard!");
}
