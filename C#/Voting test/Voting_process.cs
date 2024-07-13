namespace Voting_test
{
    public class Voting_process
    {
        public string name; // Название голосования
        public Dictionary<string, int> variants;

        // Конструктор пустого голосования
        public Voting_process(string name = "unknown")
        {
            this.name = name;
            this.variants = new Dictionary<string, int>();
        }

        // Смена название
        public void rename(string name)
        {
            this.name = name;
        }

        // Добавление варианта голосования
        public void add_variant(string variant = "unknown")
        {
            this.variants.Add(variant, 0);
        }

        // Добавить голос к пункту
        public void add_vote(string variant)
        {
            int temp = this.variants[variant];
            this.variants[variant] = ++temp;
        }

        // Подсчет голосов
        public Dictionary<string, int> show_voting()
        {
            return this.variants;
        }

        // Итог голосования
        public Tuple<string, int> show_winner()
        {
            var maxVote = variants.OrderByDescending(v => v.Value).First();
            return new Tuple<string, int>(maxVote.Key, maxVote.Value);
        }
    }
}
