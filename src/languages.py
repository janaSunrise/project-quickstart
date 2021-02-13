from dataclasses import dataclass
from textwrap import dedent


@dataclass
class Languages:
    fsharp = dedent("""
    open System
    printfn "Hello, World!"
    """)

    fortran = dedent("""
    PRINT *, "Hello World!"
    END
    """)

    objective_c = """
    #import <Foundation/Foundation.h>

    int main(int argc, const char * argv[]) {
        @autoreleasepool {
            NSLog(@"Hello World!");
        }
        return 0;
    }
    """

    abap = dedent("""
    REPORT zhelloworld
    * Write hello world to screen
    WRITE 'Hello World'.
    * Display hello world message.
    MESSAGE 'Hello World' TYPE 'I'.
    """)

    assembly = dedent("""
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
    """)

    autoit = dedent("""
    MsgBox(0, "Say Hi", "Hello World")
    """)

    basic = dedent("""
    10 PRINT "Hello, World!"
    20 END
    """)

    batch = dedent("""
    @echo off

    echo Hello World
    """)

    brainf = dedent("""
    'Hello world'
    --[>--->->->++>-<<<<<-------]
    >--.>---------.>--..+++.>----.>+++++++++.<<.+++.------.<-.>>+.
    """)

    c = dedent("""
    #include<stdio.h>

    int main(void)
    {
    printf("Hello, world!");
    return 0;
    }
    """)

    cool = dedent("""
    class Main{
    i : IO <- new IO;
    main() :Int { { i.out_string("Hello World"); 1; } };
    };
    """)

    clojurescript = '(println "Hello world!")'

    cobol = dedent("""
        IDENTIFICATION DIVISION.
        PROGRAM-ID. HelloWorld.
        PROCEDURE DIVISION.
            DISPLAY "Hello World!".
        STOP RUN.
    """)

    coffeescript = 'alert "Hello, World!"'

    cpp = dedent("""
    #include <iostream>
    using namespace std;

    int main()
    {
        cout <<"Hello World"<< endl;
        return 0;
    }
    """)

    csharp = dedent("""
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
    """)

    d = dedent("""
    import std.stdio;

    void main()
    {
        writeln("Hello World");
    }
    """)

    dart = dedent("""
    void main() {
        print('hello world');
    }
    """)

    delphi = dedent("""
    procedure TForm1.ShowAMessage;
    begin
    ShowMessage('Hello World!');
    end;
    """)

    erlang = dedent("""
    % hello world program
    -module(helloworld).
    -export([start/0]).

    start() ->
    io:fwrite("Hello, world!").
    """)

    elixir = dedent("""
    IO.puts "Hello World!"
    """)

    go = dedent("""
    package main

    import (
        "fmt"
    )

    func main() {
        fmt.Println("Hello World")
    }
    """)

    groovy = dedent("""
    class HelloWorld {
    static void main(String[] args) {
        println('Hello World');
    }
    }
    """)

    haskell = dedent("""
    main = putStrLn "Hello, World!"
    """)

    html = dedent("""
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
    """)

    intercal = dedent("""
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
    """)

    java = dedent("""
    class HelloWorld
    {
    public static void main(String[] args)
    {
        System.out.println("Hello World!!");
    }
    }
    """)

    julia = dedent("""
    println("hello world")
    """)

    juliar = dedent("""
    function main() = {
        printLine("Hello World");
    }
    """)

    javascript = dedent("""
    console.log("Hello World");
    """)

    kotlin = dedent("""
    fun main(args : Array<String>) {
        println("Hello, World!")
    }
    """)

    lisp = dedent("""
    (print "Hello World!")
    """)

    lua = dedent("""
    print("Hello World")
    """)

    ocaml = dedent("""
    print_string "Hello world";;
    """)

    nim = dedent("""
    echo "Hello World"
    """)

    pascal = dedent("""
    program Helloworld;
    begin
    writeln('hello,world!');
    end.
    """)

    php = dedent("""
    <?php
    // In PHP, we use echo to print text
    echo "Hello World";
    // If you want to print in browser's console, we use print_r
    print_r("Hello World");
    // if you want the variable data types as well use var_dump
    $stringVar = 'hello world';
    var_dump($stringVar);
    ?>
    """)

    perl = dedent("""
    #!/usr/bin/perl
    print "Hello World";
    """)

    pro = dedent("""
    message('Hello World!')
    """)

    powershell = dedent("""
    Write-Host 'Hello, World'
    """)

    python = dedent("""
    print('Hello World')
    """)

    ruby = dedent("""
    puts 'Hello World'
    """)

    rust = dedent("""
    fn main(){
    println!("Hello World!")
    }
    """)

    scala = dedent("""
    object HelloWorld extends App {
    println("Hello, World!")
    }
    """)

    r = dedent("""
    variable <- "Hello World"
    print (variable)
    """)

    sh = 'echo "Hello World"'

    sql = dedent("""
    SELECT 'Hello World';
    PRINT 'Hello World';
    """)

    swift = dedent("""
    print("Hello World!")
    """)

    typescript = dedent("""
    console.log("Hello World!");
    """)

    vb = dedent("""
    Module HelloWorld
    Sub Main( )
        System.Console.WriteLine("Hello world!")
    End Sub
    End Module
    """)
