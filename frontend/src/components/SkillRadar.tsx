import React from 'react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts';

interface SkillVector {
    skill: string;
    confidence: number; // 0.0 to 1.0
    velocity: number;   // For tooltip/color intensity
}

const SkillRadar = ({ data }: { data: SkillVector[] }) => {
    return (
        <div className="w-full h-96 bg-gray-900 rounded-xl p-4 shadow-2xl border border-gray-700">
            <h3 className="text-xl text-green-400 font-mono mb-2">Verified Vector Signature</h3>
            <ResponsiveContainer width="100%" height="100%">
                <RadarChart cx="50%" cy="50%" outerRadius="80%" data={data}>
                    <PolarGrid stroke="#374151" />
                    <PolarAngleAxis dataKey="skill" tick={{ fill: '#9CA3AF', fontSize: 12 }} />
                    <PolarRadiusAxis angle={30} domain={[0, 1]} tick={false} axisLine={false} />

                    {/* The "Shape" of the Talent */}
                    <Radar
                        name="Confidence"
                        dataKey="confidence"
                        stroke="#10B981" // Cyberpunk Green
                        strokeWidth={3}
                        fill="#10B981"
                        fillOpacity={0.3}
                    />
                </RadarChart>
            </ResponsiveContainer>

            {/* Velocity Indicator */}
            <div className="mt-4 flex justify-between text-xs text-gray-500 font-mono">
                <span>Trust Integrity: Verified (ZK-Proof)</span>
                <span>Last Updated: Real-time</span>
            </div>
        </div>
    );
};

export default SkillRadar;
