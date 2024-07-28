using Microsoft.AspNetCore.Mvc;
using System.Security.Claims;

namespace DataBasePractice.Controllers
{
    public abstract class TodoBaseControllers : Controller
    {
        protected int CurrentUserId => int.Parse(User.FindFirstValue(ClaimTypes.NameIdentifier));
    }
}