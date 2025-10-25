import React, { useState, useEffect } from "react";
import { View, Text, TextInput, Button, FlatList, StyleSheet, Alert, TouchableOpacity, ScrollView } from "react-native";
import axios from "axios";

// ------------------ API Setup ------------------
const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // replace with your backend IP if using emulator/device
});
API.interceptors.request.use((config) => {
  const token = global.token;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// ------------------ Login Component ------------------
const Login = ({ setUser }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const res = await API.post("/login/", { username, password });
      global.token = res.data.access_token;
      setUser({ username, role: "admin" });
    } catch (err) {
      Alert.alert("Login failed", "Invalid credentials");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
      <TextInput placeholder="Username" style={styles.input} value={username} onChangeText={setUsername} />
      <TextInput placeholder="Password" style={styles.input} value={password} onChangeText={setPassword} secureTextEntry />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

// ------------------ Resource Component (CRUD) ------------------
const ResourceScreen = ({ resource }) => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({ name: "", founder: "" });
  const [editId, setEditId] = useState(null);

  const fetchItems = async () => {
    setLoading(true);
    try {
      const res = await API.get(`/${resource}/`);
      setItems(res.data);
      setLoading(false);
    } catch (err) {
      setError("Failed to fetch data");
      setLoading(false);
    }
  };

  useEffect(() => { fetchItems(); }, []);

  const handleSubmit = async () => {
    try {
      if (editId) {
        await API.put(`/${resource}/${editId}/`, formData);
        setEditId(null);
      } else {
        await API.post(`/${resource}/`, formData);
      }
      setFormData({ name: "", founder: "" });
      fetchItems();
    } catch (err) {
      Alert.alert("Error", "Operation failed");
    }
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/${resource}/${id}/`);
      fetchItems();
    } catch (err) {
      Alert.alert("Error", "Delete failed");
    }
  };

  const handleEdit = (item) => {
    setEditId(item.id);
    setFormData({ name: item.name, founder: item.founder || "" });
  };

  if (loading) return <Text>Loading {resource}...</Text>;
  if (error) return <Text style={{ color: "red" }}>{error}</Text>;

  return (
    <ScrollView style={{ marginBottom: 20 }}>
      <Text style={styles.subtitle}>{resource.charAt(0).toUpperCase() + resource.slice(1)}</Text>
      <TextInput
        placeholder="Name"
        style={styles.input}
        value={formData.name}
        onChangeText={(text) => setFormData({ ...formData, name: text })}
      />
      {"founder" in formData && (
        <TextInput
          placeholder="Founder"
          style={styles.input}
          value={formData.founder}
          onChangeText={(text) => setFormData({ ...formData, founder: text })}
        />
      )}
      <Button title={editId ? "Update" : "Add"} onPress={handleSubmit} />
      <FlatList
        data={items}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.itemContainer}>
            <Text style={styles.item}>
              {item.name} {item.founder ? `(Founder: ${item.founder})` : ""}
            </Text>
            <View style={styles.buttons}>
              <Button title="Edit" onPress={() => handleEdit(item)} />
              <Button title="Delete" onPress={() => handleDelete(item.id)} />
            </View>
          </View>
        )}
      />
    </ScrollView>
  );
};

// ------------------ Main App ------------------
export default function App() {
  const [user, setUser] = useState(null);
  const [screen, setScreen] = useState("startups"); // default screen

  if (!user) return <Login setUser={setUser} />;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome {user.username}</Text>
      <View style={styles.nav}>
        {["startups", "grants", "mentors", "facilities"].map((res) => (
          <TouchableOpacity key={res} onPress={() => setScreen(res)}>
            <Text style={[styles.navItem, screen === res && styles.navActive]}>
              {res.charAt(0).toUpperCase() + res.slice(1)}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
      <Button title="Logout" onPress={() => setUser(null)} />
      <ResourceScreen resource={screen} />
    </View>
  );
}

// ------------------ Styles ------------------
const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, marginTop: 40 },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 10 },
  subtitle: { fontSize: 20, fontWeight: "600", marginTop: 20, marginBottom: 10 },
  input: { borderWidth: 1, borderColor: "#ccc", padding: 10, marginBottom: 10, borderRadius: 5 },
  item: { fontSize: 16 },
  itemContainer: { padding: 10, borderBottomWidth: 1, borderBottomColor: "#eee", flexDirection: "row", justifyContent: "space-between", alignItems: "center" },
  buttons: { flexDirection: "row", gap: 10 },
  nav: { flexDirection: "row", justifyContent: "space-around", marginVertical: 10 },
  navItem: { fontSize: 16, padding: 5 },
  navActive: { fontWeight: "bold", color: "blue" },
});
