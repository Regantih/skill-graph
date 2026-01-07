import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white selection:bg-blue-500 selection:text-white font-sans">
      {/* Navbar */}
      <nav className="fixed top-0 w-full z-50 border-b border-white/10 bg-[#0a0a0a]/80 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center">
          <div className="text-xl font-bold tracking-tight">SkillGraph</div>
          <div className="flex gap-8 text-sm font-medium text-zinc-400">
            <Link href="/onboarding" className="hover:text-white transition-colors">Agents</Link>
            <Link href="#" className="hover:text-white transition-colors">Protocol</Link>
            <Link href="/onboarding" className="px-4 py-2 bg-white text-black rounded-full hover:bg-zinc-200 transition-all">
              Sign In
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <main className="pt-32 pb-16 px-6 max-w-7xl mx-auto flex flex-col items-center text-center space-y-12">
        <div className="space-y-6 max-w-4xl flex flex-col items-center">
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight leading-[1.1]">
            A New Kind of <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">Professional Identity</span>
          </h1>
          <p className="text-xl text-zinc-400 max-w-2xl mx-auto">
            Build your verified agent. Discover experts. Stake reputation. <br />
            The decentralized talent protocol active on <strong>SkillGraph</strong>.
          </p>

          <div className="flex gap-4 pt-4">
            <Link href="/dashboard" className="px-6 py-3 bg-white text-black font-semibold rounded-full hover:bg-zinc-200 transition-all">
              Launch Dashboard
            </Link>
            <a
              href="https://github.com/Regantih/skill-graph"
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-3 border border-zinc-700 bg-zinc-900/50 text-white font-semibold rounded-full hover:bg-zinc-800 transition-all"
            >
              Documentation
            </a>
          </div>
        </div>
      </main>
    </div >
  );
}
