
import { Switch, Route } from "wouter";
import { Card, CardContent } from "@/components/ui/card";
import { AlertCircle, Loader2 } from "lucide-react";
import { ErrorBoundary } from "@/components/ErrorBoundary";
import AuthPage from "./pages/AuthPage";
import DashboardPage from "./pages/DashboardPage";
import ThreatIntelligencePage from "./pages/ThreatIntelligencePage";
import NotificationSettingsPage from "./pages/NotificationSettingsPage";
import SecurityRecommendationsPage from "./pages/SecurityRecommendationsPage";
import ThreatSocialPage from "./pages/ThreatSocialPage";
import { useUser } from "./hooks/use-user";
import { ThreatPredictionViz } from "./components/ThreatPredictionViz";
import { Helmet } from "react-helmet";

function App() {
  return (
    <ErrorBoundary>
      <Helmet>
        <title>FES Analysis Platform</title>
        <meta name="description" content="Analyze signals using FES techniques with real-time insights." />
      </Helmet>
      <AppContent />
    </ErrorBoundary>
  );
}

function AppContent() {
  const { user, isLoading, error } = useUser();

  if (isLoading) {
    return (
      <div
        className="min-h-screen w-full flex items-center justify-center bg-background"
        role="alert"
        aria-busy="true"
        aria-live="polite"
      >
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
      </div>
    );
  }

  if (error) {
    throw error; // This will be caught by ErrorBoundary
  }

  if (!user) {
    return <AuthPage />;
  }

  return (
    <Switch>
      <Route path="/" component={DashboardPage} />
      <Route
        path="/predictions"
        component={() => (
          <div className="container mx-auto p-6">
            <Helmet>
              <title>Threat Predictions - FES</title>
            </Helmet>
            <h1 className="text-2xl font-bold mb-6">Threat Predictions</h1>
            <ThreatPredictionViz />
          </div>
        )}
      />
      <Route path="/intelligence" component={ThreatIntelligencePage} />
      <Route path="/notifications" component={NotificationSettingsPage} />
      <Route path="/security" component={SecurityRecommendationsPage} />
      <Route path="/social" component={ThreatSocialPage} />
      <Route component={NotFound} />
    </Switch>
  );
}

function NotFound() {
  return (
    <div
      className="min-h-screen w-full flex items-center justify-center bg-background"
      role="alert"
      aria-live="polite"
    >
      <Card className="w-full max-w-md mx-4">
        <CardContent className="pt-6">
          <div className="flex mb-4 gap-2">
            <AlertCircle className="h-8 w-8 text-destructive" />
            <h1 className="text-2xl font-bold">404 Page Not Found</h1>
          </div>
          <p className="mt-4 text-sm text-muted-foreground">
            The requested resource could not be found.
          </p>
        </CardContent>
      </Card>
    </div>
  );
}

export default App;
