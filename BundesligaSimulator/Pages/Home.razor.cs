using Microsoft.AspNetCore.Components;

namespace BundesligaSimulator.Pages
{
    public partial  class Home : ComponentBase
    {
        enum Mode { Single, Season }
        enum Venue { Home, Away, Neutral }
        enum Rounds { HinRueck, NurHin }

        Mode current = Mode.Single;

        // Placeholder-Daten – später via API
        readonly List<string> teams = new()
    {
        "Bayern München","Borussia Dortmund","RB Leipzig","Bayer Leverkusen",
        "Eintracht Frankfurt","VfB Stuttgart","SC Freiburg","TSG Hoffenheim",
        "Borussia Mönchengladbach","1. FC Köln","Werder Bremen","VfL Wolfsburg",
        "FC Augsburg","1. FSV Mainz 05","VfL Bochum","1. FC Union Berlin",
        "Fortuna Düsseldorf","FC St. Pauli"
    };

        string teamA, teamB;
        Venue venue = Venue.Home;
        string resultSingle;

        string league = "Bundesliga (1)";
        string season = "2024/25";
        Rounds rounds = Rounds.HinRueck;
        int simulations = 10000;
        string resultSeason;

        string GetSegClass(Mode m) => $"seg-btn {(current == m ? "active" : "")}";
        string GetPillClass(bool active) => $"pill {(active ? "active" : "")}";

        // Nur UI-Feedback (kein echtes Rechnen)
        void FakeRunSingle()
        {
            if (string.IsNullOrWhiteSpace(teamA) || string.IsNullOrWhiteSpace(teamB) || teamA == teamB)
            {
                resultSingle = "Bitte zwei unterschiedliche Teams wählen.";
                return;
            }
            var ort = venue == Venue.Home ? "Team A (Heim)" : venue == Venue.Away ? "Team B (Heim)" : "neutral";
            resultSingle = $"Simulation vorbereitet: {teamA} vs {teamB} – Ort: {ort}.";
        }

        void FakeRunSeason()
        {
            resultSeason = $"Simulation vorbereitet: {league} • {season} • {rounds} • {simulations:N0} Läufe.";
        }
    }
}
