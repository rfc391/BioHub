import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Shield, AlertTriangle, Activity, Globe } from "lucide-react";
import { useQuery } from "@tanstack/react-query";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";

interface Threat {
  id: number;
  type: string;
  severity: string;
  source: string;
  targetIp: string;
  timestamp: string;
  details: {
    attackVector: string;
    indicators: string[];
  };
  status: string;
}

export default function DashboardPage() {
  const [threats, setThreats] = useState<Threat[]>([]);
  const [selectedThreat, setSelectedThreat] = useState<Threat | null>(null);

  // Fetch initial threats
  const { data: initialThreats } = useQuery({
    queryKey: ['/api/threats'],
    queryFn: async () => {
      const res = await fetch('/api/threats');
      if (!res.ok) throw new Error('Failed to fetch threats');
      return res.json() as Promise<Threat[]>;
    },
  });

  useEffect(() => {
    if (initialThreats) {
      setThreats(initialThreats);
    }
  }, [initialThreats]);

  // WebSocket connection for real-time updates
  useEffect(() => {
    const ws = new WebSocket(`ws://${window.location.host}/api/threats`);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'initial') {
        setThreats(data.threats);
      } else if (data.type === 'update') {
        setThreats(prev => [data.threat, ...prev].slice(0, 50));
      }
    };

    return () => ws.close();
  }, []);

  return (
    <div className="container mx-auto p-6">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Active Threats
            </CardTitle>
            <Shield className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">
              {threats.filter(t => t.status === 'active').length}
            </div>
            <Progress 
              value={threats.filter(t => t.severity === 'high').length / threats.length * 100} 
              className="mt-2"
            />
          </CardContent>
        </Card>

        {/* Threat Feed */}
        <div className="col-span-2 lg:col-span-3">
          <Card className="h-[600px] overflow-hidden">
            <CardHeader>
              <CardTitle>Live Threat Feed</CardTitle>
            </CardHeader>
            <CardContent className="p-0">
              <div className="h-[520px] overflow-y-auto">
                <AnimatePresence>
                  {threats.map((threat) => (
                    <motion.div
                      key={threat.id}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: 20 }}
                      className={`
                        border-b p-4 cursor-pointer hover:bg-accent
                        ${selectedThreat?.id === threat.id ? 'bg-accent' : ''}
                        ${threat.severity === 'high' ? 'border-l-4 border-l-red-500' : ''}
                      `}
                      onClick={() => setSelectedThreat(threat)}
                    >
                      <div className="flex items-center gap-4">
                        <div className={`
                          p-2 rounded-full
                          ${threat.severity === 'high' ? 'bg-red-100 text-red-600' : 'bg-yellow-100 text-yellow-600'}
                        `}>
                          <AlertTriangle className="h-4 w-4" />
                        </div>
                        <div className="flex-1">
                          <div className="flex justify-between">
                            <h3 className="font-medium">{threat.type}</h3>
                            <time className="text-sm text-muted-foreground">
                              {new Date(threat.timestamp).toLocaleTimeString()}
                            </time>
                          </div>
                          <p className="text-sm text-muted-foreground">
                            From: {threat.source} • Target: {threat.targetIp}
                          </p>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </AnimatePresence>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Selected Threat Details */}
      <AnimatePresence>
        {selectedThreat && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="mt-4"
          >
            <Card>
              <CardHeader>
                <CardTitle>Threat Details</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-2">
                  <div>
                    <h3 className="font-medium mb-2">Attack Vector</h3>
                    <p className="text-muted-foreground">{selectedThreat.details.attackVector}</p>
                  </div>
                  <div>
                    <h3 className="font-medium mb-2">Indicators</h3>
                    <ul className="list-disc list-inside text-muted-foreground">
                      {selectedThreat.details.indicators.map((indicator, i) => (
                        <li key={i}>{indicator}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
