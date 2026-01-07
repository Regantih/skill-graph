import React from 'react';
import { Terminal, ShieldCheck } from 'lucide-react';

const LOGS = [
    { sender: 'RA-Google', msg: 'QUERY: Looking for { Python > 0.9, Velocity > 2.0 }', type: 'inbound', time: '10:01 AM' },
    { sender: 'HA-Self', msg: 'MATCH: I have { Python: 0.95, Velocity: 2.4 }', type: 'outbound', time: '10:01 AM' },
    { sender: 'RA-Google', msg: 'CHALLENGE: Prove Velocity via ZK-Proof.', type: 'inbound', time: '10:02 AM' },
    { sender: 'HA-Self', msg: 'PROOF: Generated Hash #x991b... [Verified]', type: 'outbound', time: '10:02 AM' },
    { sender: 'RA-Google', msg: 'HANDSHAKE: Accepted. Scheduling Human Interview.', type: 'success', time: '10:03 AM' },
];

export default function NegotiationLog() {
    return (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 h-[400px] flex flex-col shadow-xl">
            <div className="flex items-center gap-2 mb-4 border-b border-slate-800 pb-2">
                <Terminal className="text-emerald-500" size={18} />
                <h3 className="text-sm font-bold text-slate-300">Live Negotiation Feed</h3>
            </div>

            <div className="flex-1 overflow-y-auto space-y-3 pr-2 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
                {LOGS.map((log, i) => (
                    <div key={i} className={`flex flex-col ${log.type === 'outbound' ? 'items-end' : 'items-start'}`}>
                        <div className={`max-w-[90%] rounded-lg p-3 text-xs font-mono 
              ${log.type === 'outbound' ? 'bg-emerald-900/20 border border-emerald-800 text-emerald-100' :
                                log.type === 'success' ? 'bg-indigo-900/20 border border-indigo-500 text-indigo-100' :
                                    'bg-slate-800 border border-slate-700 text-slate-300'}`}>

                            <div className="flex items-center gap-2 mb-1 opacity-50 text-[10px]">
                                <span>{log.sender}</span>
                                <span>{log.time}</span>
                            </div>

                            <div className="flex items-start gap-2">
                                {log.type === 'success' && <ShieldCheck size={14} className="text-indigo-400 mt-0.5" shrink-0 />}
                                <span>{log.msg}</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
