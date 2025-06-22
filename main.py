import sys
from utils.agent import ResearchAgent

def main():
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        print("\nGoal-Based Research Agent")
        print("=" * 50)
        print("Usage: python main.py \"Your research topic\"")
        print("\nExamples:")
        print('  python main.py "Machine learning in healthcare"')
        print('  python main.py "Renewable energy trends 2024"')
        print('  python main.py "Quantum computing applications"')
        sys.exit(1)

    topic = sys.argv[1].strip()
    agent = ResearchAgent()
    result = agent.run_research(topic)
    if result.startswith("Research failed"):
        print(f"\n{result}")
        sys.exit(1)
    print("\nResearch completed successfully!\nThe report is saved in the 'reports/' directory as a markdown file.")

if __name__ == "__main__":
    main()