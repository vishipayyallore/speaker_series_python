using System;
using static System.Console;

namespace HelloWorld
{
    class Program
    {

        static string name;
        static int id;

        static void Main(string[] args)
        {

            GetEmployeeDetails();

            ShowEmployeeDetails_x();

            WriteLine("\n\nPress any key ...");
            ReadKey();
        }


        private static void GetEmployeeDetails()
        {
            Write("Enter name: ");
            name = ReadLine();
            Write("Enter Id: ");
            id = int.Parse(ReadLine());
        }


        private static void ShowEmployeeDetails()
        {
            WriteLine($"\nDetails ----- \n\tName: {name} \n\tId: {id}");
        }


    }
}
