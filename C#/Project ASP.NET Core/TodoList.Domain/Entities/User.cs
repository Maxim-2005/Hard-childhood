namespace TodoList. Domain.Entities
{
    public class User : Entity
    {
       public string Login { get; set; }
       public string Password { get; set; }

        public User(string login, string password)
        {
            Login = login;
            Password = password;
        }
    }
}