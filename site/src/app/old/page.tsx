import { redirect } from "next/navigation";

export default function OldSiteRedirectPage() {
  redirect("/old/index.html");
}
