'use client';

import React, { useState } from 'react';

export default function ChatInterface() {
    const [messages, setMessages] = useState<{ role: 'agent' | 'user', content: string }[]>([
        { role: 'agent', content: "Hello! I'm your Talent Agent. Paste your GitHub or Portfolio link, and I'll verify your skills." }
    ]);
    const [input, setInput] = useState('');

    const handleSend = async () => {
        if (!input.trim()) return;

        // Add User Message
        const newMessages = [...messages, { role: 'user' as const, content: input }];
        setMessages(newMessages);
        setInput('');

        setMessages(prev => [...prev, { role: 'agent', content: "Verifying your profile..." }]);

        try {
            const response = await fetch('http://localhost:8000/claims/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    skill_name: "Python", // inferred for now
                    evidence_url: input,
                    user_id: "00000000-0000-0000-0000-000000000000" // mock user ID
                })
            });

            const data = await response.json();

            if (response.ok) {
                setMessages(prev => [...prev.filter(m => m.content !== "Verifying your profile..."), {
                    role: 'agent' as const,
                    content: `Verification Initiated! Claim ID: ${data.id}. Status: ${data.status}. I'm analyzing your repo now...`
                }]);
            } else {
                setMessages(prev => [...prev, { role: 'agent', content: "Error communicating with the verification network." }]);
            }
        } catch (error) {
            console.error(error);
            setMessages(prev => [...prev, { role: 'agent', content: "System Offline. Ensure Backend is running." }]);
        }
    };

    return (
        <div className="flex flex-col h-[600px] bg-slate-900 border border-slate-700 rounded-xl overflow-hidden">
            <div className="flex-1 p-6 overflow-y-auto space-y-4">
                {messages.map((msg, i) => (
                    <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`max-w-[80%] p-4 rounded-2xl ${msg.role === 'user'
                            ? 'bg-blue-600 text-white'
                            : 'bg-slate-800 text-slate-200 border border-slate-700'
                            }`}>
                            {msg.content}
                        </div>
                    </div>
                ))}
            </div>
            <div className="p-4 bg-slate-800 border-t border-slate-700">
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                        placeholder="Paste your link here..."
                        className="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <button
                        onClick={handleSend}
                        className="bg-blue-600 hover:bg-blue-500 text-white px-6 py-3 rounded-lg font-medium transition-colors"
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
}
