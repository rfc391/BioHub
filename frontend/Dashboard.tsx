import { useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { useThreats } from "@/hooks/use-threats";
import { useUser } from "@/hooks/use-user";
import { AlertCircle, LogOut, Shield, Activity } from "lucide-react";
import * as d3 from "d3";

export default function Dashboard() {
  const { threats } = useThreats();
  const { user, logout } = useUser();

  useEffect(() => {
    if (threats.length > 0) {
      renderThreatMap();
    }
  }, [threats]);

  function renderThreatMap() {
    const width = 800;
    const height = 400;

    d3.select("#threat-map").selectAll("*").remove();

    const svg = d3.select("#threat-map")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    // Enhanced dark mode visualization
    svg.append("rect")
      .attr("width", width)
      .attr("height", height)
      .attr("fill", "hsl(var(--background))");

    // Plot threat points with enhanced visibility
    threats.forEach((threat) => {
      const radius = threat.severity === "high" ? 6 : 4;

      // Add glow effect for better visibility
      svg.append("circle")
        .attr("cx", (threat.longitude + 180) * (width / 360))
        .attr("cy", (90 - threat.latitude) * (height / 180))
        .attr("r", radius + 2)
        .attr("fill", "none")
        .attr("stroke", threat.severity === "high" ? 
          "hsl(var(--destructive))" : "hsl(var(--warning))")
        .attr("stroke-opacity", 0.3)
        .attr("filter", "blur(3px)");

      svg.append("circle")
        .attr("cx", (threat.longitude + 180) * (width / 360))
        .attr("cy", (90 - threat.latitude) * (height / 180))
        .attr("r", radius)
        .attr("fill", threat.severity === "high" ? 
          "hsl(var(--destructive))" : "hsl(var(--warning))")
        .attr("opacity", 0.9);
    });

    // Add grid lines for better spatial reference
    const gridColor = "hsl(var(--muted-foreground) / 0.2)";
    for (let i = 0; i <= width; i += 80) {
      svg.append("line")
        .attr("x1", i)
        .attr("y1", 0)
        .attr("x2", i)
        .attr("y2", height)
        .attr("stroke", gridColor)
        .attr("stroke-width", 0.5);
    }
    for (let i = 0; i <= height; i += 40) {
      svg.append("line")
        .attr("x1", 0)
        .attr("y1", i)
        .attr("x2", width)
        .attr("y2", i)
        .attr("stroke", gridColor)
        .attr("stroke-width", 0.5);
    }
  }

  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="border-b border-border/50 backdrop-blur-sm bg-background/95 sticky top-0 z-50">
        <div className="container mx-auto flex justify-between items-center h-16 px-4">
          <div className="flex items-center gap-2">
            <Shield className="h-6 w-6 text-primary" />
            <h1 className="text-xl font-bold">Cyber Command</h1>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-sm text-muted-foreground">
              Welcome, {user?.username}
            </span>
            <Button variant="outline" size="sm" onClick={() => logout()}>
              <LogOut className="h-4 w-4 mr-2" />
              Logout
            </Button>
          </div>
        </div>
      </header>

      <main className="container mx-auto p-4 grid gap-4 grid-cols-1 lg:grid-cols-3">
        <Card className="lg:col-span-2 border-border/50 bg-card/95 backdrop-blur-sm">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Activity className="h-5 w-5" />
              Global Threat Map
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div id="threat-map" className="w-full aspect-video bg-background rounded-lg border border-border/50" />
          </CardContent>
        </Card>

        <Card className="border-border/50 bg-card/95 backdrop-blur-sm">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <AlertCircle className="h-5 w-5" />
              Active Threats
            </CardTitle>
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[500px] pr-4">
              {threats.map((threat, i) => (
                <div
                  key={i}
                  className="flex items-start gap-2 p-3 border-b border-border/50 last:border-0 hover:bg-muted/50 transition-colors"
                >
                  <AlertCircle className={
                    threat.severity === "high" 
                      ? "text-destructive animate-pulse" 
                      : "text-warning"
                  } />
                  <div>
                    <p className="font-medium">{threat.type}</p>
                    <p className="text-sm text-muted-foreground">
                      {threat.location} - {threat.timestamp}
                    </p>
                  </div>
                </div>
              ))}
            </ScrollArea>
          </CardContent>
        </Card>
      </main>
    </div>
  );
}