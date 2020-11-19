from dataclasses import dataclass


@dataclass
class Languages:
    fsharp = """
    open System
    printfn "Hello, World!"
    """

    fortran = """
    PRINT *, "Hello World!"
    END
    """

    objective_c = """
    #import <Foundation/Foundation.h>

    int main(int argc, const char * argv[]) {
        @autoreleasepool {
            NSLog(@"Hello World!");
        }
        return 0;
    }
    """

    abap = """
    REPORT zhelloworld
    * Write hello world to screen
    WRITE 'Hello World'.
    * Display hello world message.
    MESSAGE 'Hello World' TYPE 'I'.
    """

    assembly = """
    .model small
    .data
            msg db 10d,13d,"Hello World$"

    .code
            mov ax,@data
            mov ds,ax

            lea dx,msg
            mov ah,09h
            int 21h

            mov ah,4ch
            int 21h
    end
    """

    autoit = """
    MsgBox(0, "Say Hi", "Hello World")
    """

    basic = """
    10 PRINT "Hello, World!"
    20 END
    """

    batch = """
    @echo off

    echo Hello World
    """

    brainf = """
    'Hello world'
    --[>--->->->++>-<<<<<-------]
    >--.>---------.>--..+++.>----.>+++++++++.<<.+++.------.<-.>>+.
    """

    c = """
    #include<stdio.h>

    int main(void)
    {
    printf("Hello, world!");
    return 0;
    }
    """

    cool = """
    class Main{
    i : IO <- new IO;
    main() :Int { { i.out_string("Hello World"); 1; } };
    };
    """

    clojurescript = '(println "Hello world!")'

    cobol = """
        IDENTIFICATION DIVISION.
        PROGRAM-ID. HelloWorld.
        PROCEDURE DIVISION.
            DISPLAY "Hello World!".
        STOP RUN.
    """

    coffeescript = 'alert "Hello, World!"'

    cpp = """
    #include <iostream>
    using namespace std;

    int main()
    {
        cout <<"Hello World"<< endl;
        return 0;
    }
    """

    csharp = """
    using System;

    namespace helloWorld
    {
        class HelloWorld
        {
            static void Main(string[] args)
            {
                Console.WriteLine("Hello World!");
            }
        }
    }
    """

    d = """
    import std.stdio;

    void main()
    {
        writeln("Hello World");
    }
    """

    dart = """
    void main() {
        print('hello world');
    }
    """

    delphi = """
    procedure TForm1.ShowAMessage;
    begin
    ShowMessage('Hello World!');
    end;
    """

    erlang = """
    % hello world program
    -module(helloworld).
    -export([start/0]).

    start() ->
    io:fwrite("Hello, world!").
    """

    elixir = """
    IO.puts "Hello World!"
    """

    go = """
    package main

    import (
        "fmt"
    )

    func main() {
        fmt.Println("Hello World")
    }
    """

    groovy = """
    class HelloWorld {
    static void main(String[] args) {
        println('Hello World');
    }
    }
    """

    haskell = """
    main = putStrLn "Hello, World!"
    """

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Hello World!</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    """

    intercal = """
    DO ,1 <- #13
    PLEASE DO ,1 SUB #1 <- #238
    DO ,1 SUB #2 <- #108
    DO ,1 SUB #3 <- #112
    DO ,1 SUB #4 <- #0
    DO ,1 SUB #5 <- #64
    DO ,1 SUB #6 <- #194
    DO ,1 SUB #7 <- #48
    PLEASE DO ,1 SUB #8 <- #22
    DO ,1 SUB #9 <- #248
    DO ,1 SUB #10 <- #168
    DO ,1 SUB #11 <- #24
    DO ,1 SUB #12 <- #16
    DO ,1 SUB #13 <- #162
    PLEASE READ OUT ,1
    PLEASE GIVE UP
    """

    java = """
    class HelloWorld
    {
    public static void main(String[] args)
    {
        System.out.println("Hello World!!");
    }
    }
    """

    julia = """
    println("hello world")
    """

    juliar = """
    function main() = {
        printLine("Hello World");
    }
    """

    javascript = """
    console.log("Hello World");
    """

    kotlin = """
    fun main(args : Array<String>) {
        println("Hello, World!")
    }
    """

    lisp = """
    (print "Hello World!")
    """

    lua = """
    print("Hello World")
    """

    ocaml = """
    print_string "Hello world";;
    """

    nim = """
    echo "Hello World"
    """

    pascal = """
    program Helloworld;
    begin
    writeln('hello,world!');
    end.
    """

    php = """
    <?php
    // In PHP, we use echo to print text
    echo "Hello World";
    // If you want to print in browser's console, we use print_r
    print_r("Hello World");
    // if you want the variable data types as well use var_dump
    $stringVar = 'hello world';
    var_dump($stringVar);
    ?>
    """

    perl = """
    #!/usr/bin/perl
    print "Hello World";
    """

    pro = """
    message('Hello World!')
    """

    powershell = """
    Write-Host 'Hello, World'
    """

    python = """
    print('Hello World')
    """

    ruby = """
    puts 'Hello World'
    """

    rust = """
    fn main(){
    println!("Hello World!")
    }
    """

    scala = """
    object HelloWorld extends App {
    println("Hello, World!")
    }
    """

    r = """
    variable <- "Hello World"
    print (variable)
    """

    sh = 'echo "Hello World"'

    sql = """
    SELECT 'Hello World';
    PRINT 'Hello World';
    """

    swift = """
    print("Hello World!")
    """

    typescript = """
    console.log("Hello World!");
    """

    vb = """
    Module HelloWorld
    Sub Main( )
        System.Console.WriteLine("Hello world!")
    End Sub
    End Module
    """
