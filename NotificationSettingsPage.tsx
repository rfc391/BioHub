import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { useQuery, useMutation } from "@tanstack/react-query";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel } from "@/components/ui/form";
import { useToast } from "@/hooks/use-toast";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { Bell, Mail, Webhook, Clock } from "lucide-react";

const notificationPreferencesSchema = z.object({
  emailEnabled: z.boolean(),
  webhookEnabled: z.boolean(),
  inAppEnabled: z.boolean(),
  emailAddress: z.string().email().optional().nullable(),
  webhookUrl: z.string().url().optional().nullable(),
  minimumSeverity: z.enum(["low", "medium", "high"]),
  digestFrequency: z.enum(["realtime", "hourly", "daily"]),
  quietHoursStart: z.number().min(0).max(23).optional().nullable(),
  quietHoursEnd: z.number().min(0).max(23).optional().nullable(),
});

type NotificationPreferences = z.infer<typeof notificationPreferencesSchema>;

export default function NotificationSettingsPage() {
  const { toast } = useToast();
  const form = useForm<NotificationPreferences>({
    resolver: zodResolver(notificationPreferencesSchema),
    defaultValues: {
      emailEnabled: true,
      webhookEnabled: false,
      inAppEnabled: true,
      minimumSeverity: "medium",
      digestFrequency: "realtime",
    },
  });

  const { data: preferences, isLoading } = useQuery({
    queryKey: ["/api/notifications/preferences"],
    queryFn: async () => {
      const res = await fetch("/api/notifications/preferences");
      if (!res.ok) throw new Error("Failed to fetch preferences");
      return res.json();
    },
  });

  const mutation = useMutation({
    mutationFn: async (data: NotificationPreferences) => {
      const res = await fetch("/api/notifications/preferences", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error("Failed to update preferences");
      return res.json();
    },
    onSuccess: () => {
      toast({
        title: "Success",
        description: "Notification preferences updated successfully",
      });
    },
    onError: () => {
      toast({
        title: "Error",
        description: "Failed to update notification preferences",
        variant: "destructive",
      });
    },
  });

  useEffect(() => {
    if (preferences) {
      form.reset(preferences);
    }
  }, [preferences, form]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary" />
      </div>
    );
  }

  return (
    <div className="container mx-auto p-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Bell className="h-5 w-5" />
            Notification Preferences
          </CardTitle>
        </CardHeader>
        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit((data) => mutation.mutate(data))} className="space-y-6">
              {/* Email Notifications */}
              <div className="space-y-4">
                <h3 className="text-lg font-medium flex items-center gap-2">
                  <Mail className="h-5 w-5" />
                  Email Notifications
                </h3>
                <FormField
                  control={form.control}
                  name="emailEnabled"
                  render={({ field }) => (
                    <FormItem className="flex items-center justify-between rounded-lg border p-4">
                      <div className="space-y-0.5">
                        <FormLabel>Enable Email Notifications</FormLabel>
                        <FormDescription>
                          Receive threat alerts via email
                        </FormDescription>
                      </div>
                      <FormControl>
                        <Switch
                          checked={field.value}
                          onCheckedChange={field.onChange}
                        />
                      </FormControl>
                    </FormItem>
                  )}
                />
                {form.watch("emailEnabled") && (
                  <FormField
                    control={form.control}
                    name="emailAddress"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Email Address</FormLabel>
                        <FormControl>
                          <Input {...field} type="email" placeholder="your@email.com" />
                        </FormControl>
                      </FormItem>
                    )}
                  />
                )}
              </div>

              {/* Webhook Notifications */}
              <div className="space-y-4">
                <h3 className="text-lg font-medium flex items-center gap-2">
                  <Webhook className="h-5 w-5" />
                  Webhook Notifications
                </h3>
                <FormField
                  control={form.control}
                  name="webhookEnabled"
                  render={({ field }) => (
                    <FormItem className="flex items-center justify-between rounded-lg border p-4">
                      <div className="space-y-0.5">
                        <FormLabel>Enable Webhook Notifications</FormLabel>
                        <FormDescription>
                          Send alerts to your webhook endpoint
                        </FormDescription>
                      </div>
                      <FormControl>
                        <Switch
                          checked={field.value}
                          onCheckedChange={field.onChange}
                        />
                      </FormControl>
                    </FormItem>
                  )}
                />
                {form.watch("webhookEnabled") && (
                  <FormField
                    control={form.control}
                    name="webhookUrl"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Webhook URL</FormLabel>
                        <FormControl>
                          <Input {...field} type="url" placeholder="https://your-webhook.com/endpoint" />
                        </FormControl>
                      </FormItem>
                    )}
                  />
                )}
              </div>

              {/* Notification Settings */}
              <div className="space-y-4">
                <h3 className="text-lg font-medium flex items-center gap-2">
                  <Clock className="h-5 w-5" />
                  Notification Settings
                </h3>
                <div className="grid gap-4 md:grid-cols-2">
                  <FormField
                    control={form.control}
                    name="minimumSeverity"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Minimum Severity</FormLabel>
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <FormControl>
                            <SelectTrigger>
                              <SelectValue />
                            </SelectTrigger>
                          </FormControl>
                          <SelectContent>
                            <SelectItem value="low">Low</SelectItem>
                            <SelectItem value="medium">Medium</SelectItem>
                            <SelectItem value="high">High</SelectItem>
                          </SelectContent>
                        </Select>
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name="digestFrequency"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Notification Frequency</FormLabel>
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <FormControl>
                            <SelectTrigger>
                              <SelectValue />
                            </SelectTrigger>
                          </FormControl>
                          <SelectContent>
                            <SelectItem value="realtime">Real-time</SelectItem>
                            <SelectItem value="hourly">Hourly Digest</SelectItem>
                            <SelectItem value="daily">Daily Digest</SelectItem>
                          </SelectContent>
                        </Select>
                      </FormItem>
                    )}
                  />
                </div>
              </div>

              <Button type="submit" className="w-full">
                Save Preferences
              </Button>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
}
