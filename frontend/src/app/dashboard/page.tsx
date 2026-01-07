"use client";

import React, { useState, useEffect } from 'react';
import SkillRadar from '../../components/SkillRadar';
import NegotiationLog from '../../components/NegotiationLog';
import { Activity, Zap, Cpu, Network } from 'lucide-react';
import { motion } from 'framer-motion';

interface MarketTrend {
    skill: string;
    demand_score: number;
    match_count: number;
}

export default function AgentDashboard() {
    const [marketData, setMarketData] = useState<MarketTrend | null>(null);

    // Mock Radar Data for the specific user "Hemanth Reganti"
    const radarData = [
        { skill: 'Python', confidence: 0.95, velocity: 0.8 },
        { skill: 'System Design', confidence: 0.88, velocity: 0.7 },
        { skill: 'AI/LLMs', confidence: 0.92, velocity: 0.95 },
        { skill: 'React', confidence: 0.75, velocity: 0.5 },
        { skill: 'DevOps', confidence: 0.70, velocity: 0.4 },
        { skill: 'Leadership', confidence: 0.85, velocity: 0.6 },
    ];

    useEffect(() => {
        async function fetchMarketDemand() {
            try {
                // Simulating the API response for now
                // In real deployment: const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/market/scout?skill=AI/LLMs`);
                await new Promise(r => setTimeout(r, 1200)); // Network delay simulation
                const mockResponse = { skill: 'AI/LLMs', demand_score: 94, match_count: 12 };
                setMarketData(mockResponse);
            } catch (err) {
                console.error("Failed to sync with Market", err);
            }
        }
        fetchMarketDemand();
    }, []);

    return (
        <div className="min-h-screen bg-[#050505] text-white p-6 md:p-10 font-sans">
            <header className="mb-10 flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-emerald-400 to-cyan-400 mb-1">
                        Agent Command Center
                    </h1>
                    <p className="text-zinc-500 text-sm font-mono">ID: HA-REGANTI-X99 | STATUS: ACTIVE_HUNTING</p>
                </div>
                <div className="flex items-center gap-3">
                    <span className="flex h-2 w-2 relative">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    <span className="text-xs text-emerald-400 font-mono">LIVE LINK UPLINK</span>
                </div>
            </header>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                {/* Left Column: Stats & Radar */}
                <div className="lg:col-span-4 space-y-6">

                    {/* Market Demand Card */}
                    <motion.div
                        initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.5 }}
                        className="bg-gradient-to-br from-indigo-900/40 to-slate-900 border border-indigo-500/30 rounded-2xl p-6 relative overflow-hidden shadow-lg h-48"
                    >
                        <div className="relative z-10">
                            <div className="flex items-center gap-2 mb-3">
                                <Activity className="text-indigo-400" size={20} />
                                <h3 className="text-md font-medium text-indigo-100">Market Demand Live</h3>
                            </div>

                            {marketData ? (
                                <>
                                    <p className="text-sm text-slate-300 mb-4 leading-relaxed">
                                        Your <span className="text-white font-bold">"{marketData.skill}"</span> vector is currently sought by <span className="text-indigo-300 font-mono text-lg">{marketData.demand_score}</span> active agents.
                                    </p>
                                    <button className="text-xs bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded transition-colors flex items-center gap-2">
                                        View {marketData.match_count} Matches <Zap size={12} />
                                    </button>
                                </>
                            ) : (
                                <div className="flex flex-col gap-2 mt-4">
                                    <div className="h-4 bg-indigo-500/20 rounded animate-pulse w-3/4"></div>
                                    <div className="h-4 bg-indigo-500/20 rounded animate-pulse w-1/2"></div>
                                    <p className="text-xs text-indigo-400/50 mt-2 font-mono">Syncing Discovery Platform...</p>
                                </div>
                            )}
                        </div>
                        {/* Background Glow */}
                        <div className="absolute -right-10 -bottom-10 w-32 h-32 bg-indigo-600 blur-[80px] opacity-30"></div>
                    </motion.div>

                    {/* Velocity Stat */}
                    <motion.div
                        initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.5, delay: 0.1 }}
                        className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-6 relative overflow-hidden"
                    >
                        <div className="flex items-center justify-between mb-2">
                            <div className="flex items-center gap-2">
                                <Cpu className="text-cyan-400" size={20} />
                                <h3 className="text-md font-medium text-zinc-200">Learning Velocity</h3>
                            </div>
                            <span className="text-2xl font-bold text-cyan-400 font-mono">2.4x</span>
                        </div>
                        <div className="w-full bg-zinc-800 h-2 rounded-full overflow-hidden mt-2">
                            <div className="bg-cyan-500 h-full w-[85%] rounded-full shadow-[0_0_10px_rgba(6,182,212,0.5)]"></div>
                        </div>
                        <p className="text-xs text-zinc-500 mt-3 font-mono">
                            Top 5% of 'Generative AI' learners. <br />Based on recent GitHub activity density.
                        </p>
                    </motion.div>

                </div>

                {/* Center Column: Radar Chart */}
                <div className="lg:col-span-4">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}
                    >
                        <SkillRadar data={radarData} />
                    </motion.div>
                </div>

                {/* Right Column: Negotiation Log */}
                <div className="lg:col-span-4">
                    <motion.div
                        initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.7 }}
                    >
                        <div className="bg-emerald-900/10 border border-emerald-900/50 rounded-2xl p-1 mb-4">
                            <div className="px-4 py-2 flex items-center justify-between">
                                <div className="flex items-center gap-2">
                                    <Network className="text-emerald-500" size={16} />
                                    <span className="text-xs font-mono text-emerald-400">NEGOTIATION_CHANNEL_SECURE</span>
                                </div>
                                <span className="text-[10px] text-emerald-600 font-mono">ENCRYPTED</span>
                            </div>
                        </div>
                        <NegotiationLog />
                    </motion.div>
                </div>
            </div>
        </div>
    );
}
