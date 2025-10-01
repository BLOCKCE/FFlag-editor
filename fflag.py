import json
import re
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from collections import OrderedDict
import os
import stat
import sys

default = {
    "FFlagFilterPurchasePromptInputDispatch_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;532319696;flagbank",
    "FFlagRemovePermissionsButtons_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1743048710;flagbank",
    "FFlagPlayerListReduceRerenders_IXPValue": "false;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;673415276;flagbank",
    "FFlagAvatarEditorPromptsNoPromptNoRender_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;347969450;flagbank",
    "FFlagPlayerListClosedNoRenderWithTenFoot_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;673415276;flagbank",
    "FFlagUseUserProfileStore4_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1811976791;flagbank",
    "FFlagPublishAssetPromptNoPromptNoRender_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;347969450;flagbank",
    "FFlagUseNewPlayerList3_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1196207538;flagbank",
    "FFlagFixLeaderboardCleanup_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1196207538;flagbank",
    "FFlagMoveNewPlayerListDividers_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1196207538;flagbank",
    "FFlagFixLeaderboardStatSortTypeMismatch_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1196207538;flagbank",
    "FFlagFilterNewPlayerListValueStat_IXPValue": "true;1;InExperience.Performance;InExperience.Performance.Holdout.June2025.CoreUIOnly;1196207538;flagbank",
    "FFlagUnreduxChatTransparencyV2_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;1952442096;flagbank",
    "FFlagExpChatRemoveMessagesFromAppContainer_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;878331096;flagbank",
    "FFlagChatWindowOnlyRenderMessagesOnce_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;530774716;flagbank",
    "FFlagUnreduxLastInputTypeChanged_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;510908202;flagbank",
    "FFlagChatWindowSemiRoduxMessages_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;77621948;flagbank",
    "FFlagInitializeAutocompleteOnlyIfEnabled_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;1049260247;flagbank",
    "FFlagChatWindowMessageRemoveState_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;1376708965;flagbank",
    "FFlagExpChatUseVoiceParticipantsStore2_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;125421786;flagbank",
    "FFlagExpChatMemoBillboardGui_IXPValue": "false;1;ExperienceChat.Performance;FeatureRollout;2065932627;flagbank",
    "FFlagExpChatRemoveBubbleChatAppUserMessagesState_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;2065932627;flagbank",
    "FFlagEnableLeaveGameUpsellEntrypoint_IXPValue": "false;1;ExperienceChat.Performance;FeatureRollout;90111814;flagbank",
    "FFlagExpChatUseAdorneeStoreV4_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;726159443;flagbank",
    "FFlagEnableChatMicPerfBinding_IXPValue": "true;1;ExperienceChat.Performance;FeatureRollout;1740143267;flagbank",
    "FFlagEnableCreatorSubtitleNavigation_v2_IXPValue": "true;1;PlayerApp.GameDetailsPage.Exposure;Discovery.EDP.MediaGalleryVideoPreview.v3;1531928792;flagbank",
    "FFlagChatOptimizeCommandProcessing_IXPValue": "true;1;ChatWindow.Performance;FeatureRollout;288906352;flagbank",
    "FFlagMemoizeChatReportingMenu_IXPValue": "true;1;ChatWindow.Performance;FeatureRollout;1915032136;flagbank",
    "FFlagMemoizeChatInputApp_IXPValue": "true;1;ChatWindow.Performance;FeatureRollout;1529984850;flagbank",
    "FFlagUseUserProfileStore4_IXPValue": "true;1;ChatWindow.Performance;FeatureRollout;1811976791;flagbank",
    "FFlagVideoHandleEarlyServiceShutdown_IXPValue": "true;1;Portal.VideoPlaybackManagerWithEarlyServiceShutdownHandling-1758059695;VideoPlaybackManagerWithEarlyServiceShutdownHandling;141700402;flagbank",
    "FFlagVideoPlaybackManager2_IXPValue": "true;1;Portal.VideoPlaybackManagerWithEarlyServiceShutdownHandling-1758059695;VideoPlaybackManagerWithEarlyServiceShutdownHandling;1210184318;flagbank",
    "FFlagAppChatNewChatInputBar2_IXPValue": "true;1;Social.AppChat;AppChat.NewChatInputBar;1798109022;dev_controlled",
    "FFlagAppChatNewChatInputBarIxpEnabled_IXPValue": "true;1;Social.AppChat;AppChat.NewChatInputBar;1798109022;dev_controlled",
    "FFlagAppChatRemoveUserProfileTitles2_IXPValue": "true;1;Party.Chat.Performance;FeatureRollout;568652191;dev_controlled",
    "FFlagMacUnifyKeyCodeMapping_IXPValue": "true;1;Portal.MacUnifyKeyCodeMapping-1752599684;FeatureRollout;965638851;flagbank",
    "FFlagProfilePlatformEnableClickToCopyUsername_IXPValue": "true;1;Social.ProfilePeekView;Social.ProfileBackgrounds.GiveViewersAccessToNewBackgrounds;698399716;dev_controlled",
    "FFlagPPVBackgroundEnabled_IXPValue": "true;1;Social.ProfilePeekView;Social.ProfileBackgrounds.GiveViewersAccessToNewBackgrounds;766322282;dev_controlled",
    "FFlagAddPriceBelowCurrentlyWearing_IXPValue": "true;1;Social.Profile.Inventory;FeatureRollout;650888593;flagbank",
    "FFlagEnableDoubleNotifRegistrationFixV2_IXPValue": "true;1;Portal.EnableDoubleNotifRegistrationFixV2-1752599897;FeatureRollout;1249476439;flagbank",
    "FFlagEnableNotApprovedPageV2_IXPValue": "true;1;UserSafety.NotApprovedPage.UserID;UserSafety.NotApprovedPage.UserID.NotApprovedPageRedesign.2025Q3;1032022767;dev_controlled",
    "FFlagEnableNapIxpLayerExposure_IXPValue": "true;1;UserSafety.NotApprovedPage.UserID;UserSafety.NotApprovedPage.UserID.NotApprovedPageRedesign.2025Q3;1032022767;dev_controlled"
}



home_dir = os.path.expanduser("~")
roblox_path = os.path.join(home_dir, r"AppData\Local\Roblox")

if not os.path.exists(roblox_path):
    messagebox.showwarning("Roblox not found", "Please install Roblox")
    sys.exit(0)

file_path = os.path.join(roblox_path, r"ClientSettings\IxpSettings.json")

if not os.path.exists(file_path):
    print("File does not exist, creating it.")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    open(file_path, 'w').close()

PAIR_RE = re.compile(r'"(?P<k>[^"\\]+)"\s*:\s*"(?P<v>[^"\\]*)"')



class AddNewDialog(tk.Toplevel):
    def __init__(self, master, on_add_callback):
        super().__init__(master)
        self.title("Add Fast Flag")
        self.geometry("400x260")
        self.resizable(True, True)
        self.on_add = on_add_callback
        self.transient(master)
        self.grab_set()

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=12, pady=12)

        self.single_tab = ttk.Frame(notebook)
        notebook.add(self.single_tab, text="Add single")

        frm_single = ttk.Frame(self.single_tab)
        frm_single.pack(fill="x", padx=4, pady=4)

        ttk.Label(frm_single, text="Name").grid(row=0, column=0, sticky="w", padx=(0,8), pady=(0,6))
        self.e_name = ttk.Entry(frm_single, width=36)
        self.e_name.grid(row=0, column=1, sticky="ew", pady=(0,6))

        ttk.Label(frm_single, text="Value").grid(row=1, column=0, sticky="w", padx=(0,8))
        self.e_value = ttk.Entry(frm_single, width=36)
        self.e_value.grid(row=1, column=1, sticky="ew")

        frm_single.columnconfigure(1, weight=1)

        ttk.Button(self.single_tab, text="Add", command=self._add_single).pack(side="right", padx=4, pady=(8,8))

        self.import_tab = ttk.Frame(notebook)
        notebook.add(self.import_tab, text="Import JSON")

        self.txt_json = tk.Text(self.import_tab, width=40, height=6, wrap="none")
        self.txt_json.pack(fill="both", expand=True, padx=4, pady=4)
        ttk.Button(self.import_tab, text="Import", command=self._import_json).pack(side="right", padx=4, pady=(0,8))

        footer = ttk.Frame(self)
        footer.pack(fill="x", padx=12, pady=(0,12))
        ttk.Button(footer, text="Close", command=self.destroy).pack(side="right")

        self.bind("<Return>", lambda e: self._add_single() if notebook.index("current") == 0 else self._import_json())
        self.e_name.focus_set()

    def _add_single(self):
        name = self.e_name.get().strip()
        value = self.e_value.get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Please enter a flag name.")
            return
        try:
            self.on_add(name, value)
            self.destroy()  # auto-close after adding
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _import_json(self):
        raw = self.txt_json.get("1.0", tk.END).strip()
        if not raw:
            messagebox.showwarning("Empty", "Paste data to import.")
            return
        added = 0
        # strict JSON first
        try:
            parsed = json.loads(raw)
            items = []
            if isinstance(parsed, dict):
                items = list(parsed.items())
            elif isinstance(parsed, list):
                for obj in parsed:
                    if isinstance(obj, dict):
                        items.extend(obj.items())
            else:
                raise ValueError
            for k, v in items:
                self.on_add(str(k), str(v))
                added += 1
        except Exception:
            # relaxed pairs fallback
            for k, v in PAIR_RE.findall(raw):
                self.on_add(k, v)
                added += 1
        if added:
            messagebox.showinfo("Imported", f"Added {added} item" + ("" if added==1 else "s"))
            self.destroy()  # auto-close after import
        else:
            messagebox.showerror("Invalid input", "No pairs like \"KEY\":\"VALUE\" found.")

class FastFlagManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FastFlag Manager")
        self.geometry("560x360")
        self.minsize(520, 320)

        self.flags: OrderedDict[str, str] = OrderedDict()

        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x", padx=10, pady=8)

        ttk.Button(toolbar, text="+ Add new", command=self.open_add_dialog).pack(side="left")
        ttk.Button(toolbar, text="Delete selected", command=self.delete_selected).pack(side="left", padx=(8,0))
        ttk.Button(toolbar, text="Delete all", command=self.delete_all).pack(side="left", padx=(8,0))
        ttk.Button(toolbar, text="Save", command=self.write_ixp_settings).pack(side="right")

        columns = ("name", "value")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="extended")
        self.tree.heading("name", text="Name")
        self.tree.heading("value", text="Value")
        self.tree.column("name", width=280, anchor="w")
        self.tree.column("value", width=240, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0,10))

        # inline edit support
        self.editor = None
        self.tree.bind('<Double-1>', self._begin_edit)
        self.tree.bind('<Return>', self._begin_edit)

        self.status = ttk.Label(self, text="0 items", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0,8))

        self.bind("<Delete>", lambda e: self.delete_selected())

        diffs = self.diff_ixp_settings()

        for name, value in diffs.items():
            self.add_flag(name, value)

    def open_add_dialog(self):
        AddNewDialog(self, self.add_flag)

    def add_flag(self, name: str, value: str):
        self.flags[name] = value
        self._refresh_tree()

    def delete_selected(self):
        selection = self.tree.selection()
        if not selection:
            return
        for iid in selection:
            name = self.tree.set(iid, "name")
            if name in self.flags:
                del self.flags[name]
        self._refresh_tree()

    def delete_all(self):
        if not self.flags:
            return
        if messagebox.askyesno("Delete all", "Are you sure you want to remove all entries?"):
            self.flags.clear()
            self._refresh_tree()

    def write_ixp_settings(self):
        merged_data = {**default, **self.flags}

        if not file_path:
            return
        try:
            os.chmod(file_path, stat.S_IWRITE)
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(merged_data, f, indent=4)
                
            os.chmod(file_path, stat.S_IREAD)
            messagebox.showinfo("Saved", f"Saved {len(self.flags)} entr" + ("y" if len(self.flags)==1 else "ies"))
        except Exception as e:
            messagebox.showerror("Save failed", str(e))

    def diff_ixp_settings(self):

        if not os.path.exists(file_path):
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
        except Exception as e:
            print(f"Failed to load {file_path}: {e}")
            return {}

        differences = {}

        for key, file_value in file_data.items():
            if key not in default or default[key] != file_value:
                differences[key] = file_value

        for key, expected_value in default.items():
            if key not in file_data:
                differences[key] = expected_value

        return differences

    def save_to_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Save flags to JSON",
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.flags, f, indent=2)
            messagebox.showinfo("Saved", f"Saved {len(self.flags)} entr" + ("y" if len(self.flags)==1 else "ies") + f" to\n{path}")
        except Exception as e:
            messagebox.showerror("Save failed", str(e))

    def _refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for name, value in self.flags.items():
            self.tree.insert("", tk.END, values=(name, value))
        self.status.config(text=f"{len(self.flags)} item" + ("" if len(self.flags)==1 else "s"))

    # inline editor methods
    def _begin_edit(self, event):
        region = self.tree.identify('region', event.x, event.y)
        if region != 'cell':
            iid = self.tree.focus()
            if not iid:
                return
            col = self.tree.identify_column(event.x) or '#2'
        else:
            iid = self.tree.identify_row(event.y)
            col = self.tree.identify_column(event.x)
        if not iid or col not in ('#1', '#2'):
            return
        x, y, w, h = self.tree.bbox(iid, col)
        value = self.tree.set(iid, column=col)
        self._end_edit()
        self.editor = tk.Entry(self.tree)
        self.editor.insert(0, value)
        self.editor.select_range(0, tk.END)
        self.editor.focus()
        self.editor.place(x=x, y=y, width=w, height=h)
        self.editor.bind('<Return>', lambda e: self._commit_edit(iid, col))
        self.editor.bind('<KP_Enter>', lambda e: self._commit_edit(iid, col))
        self.editor.bind('<Escape>', lambda e: self._end_edit())
        self.editor.bind('<FocusOut>', lambda e: self._commit_edit(iid, col))

    def _commit_edit(self, iid, col):
        if not self.editor:
            return
        new_val = self.editor.get()
        old_name = self.tree.set(iid, 'name')
        if col == '#1':
            new_name = new_val.strip()
            if not new_name:
                self._end_edit(); return
            current_value = self.flags.pop(old_name, self.tree.set(iid, 'value'))
            self.flags[new_name] = current_value
        else:
            self.flags[old_name] = new_val
        self._end_edit()
        self._refresh_tree()

    def _end_edit(self):
        if self.editor is not None:
            self.editor.destroy()
            self.editor = None

if __name__ == "__main__":
    app = FastFlagManager()
    app.mainloop()








user_data = {
    "FFlagRemoveMeInParent2":"false",
}
write_ixp_settings(user_data)