using Voting_test;
using static System.Runtime.InteropServices.JavaScript.JSType;

class Voting
{
    static void Main(string[] args)
    {
        // Создаем голосование
        Voting_process vote = new Voting_process("opros");
        Console.WriteLine(vote.name);
        
        // Переименовали голосование
        vote.name = "New name";
        Console.WriteLine(vote.name);

        // Добавляем пункты голосования
        vote.add_variant("За гречку");
        vote.add_variant("За рис");
        vote.add_variant("За борщ");

        // Выводим результаты голосования
        Dictionary<string, int> dict = vote.show_voting();
        foreach (var e in dict)
        {
            Console.WriteLine(e);
        }

        // Добавляем голоса
        vote.add_vote("За борщ");
        vote.add_vote("За борщ");
        vote.add_vote("За борщ");
        vote.add_vote("За борщ");
        vote.add_vote("За рис");
        vote.add_vote("За рис");
        vote.add_vote("За рис");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");
        vote.add_vote("За гречку");

        foreach (var e in dict)
        {
            Console.WriteLine(e);
        }

        // Вывод победителя
        Console.WriteLine("В голосовании победил вариант:");
        Console.WriteLine(vote.show_winner());
    }
}